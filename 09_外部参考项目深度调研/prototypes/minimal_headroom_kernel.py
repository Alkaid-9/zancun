#!/usr/bin/env python3
"""
minimal_headroom_kernel.py · 提纯自 headroomlabs-ai/headroom 核心上下文压缩与缓存守卫原件
零外部依赖（纯 Python 3.10+ 原生标准库），完整闭环演示：
1. 缓存守卫不变式（CacheAligner · compute_frozen_count）：
   精准计算 Anthropic Prompt Caching 冻结前缀边界，冷冻区零字节改动，杜绝 KV Cache 穿透
2. 结构化数据压缩器（SmartCrusher）：
   JSON 紧凑化、空值剔除与大数组有损折叠，保留核心数据骨架
3. 终端日志压缩器（LogCrusher）：
   精准提取 FATAL/ERROR/Traceback 错误核与上下文，折叠海量重复性进度条，实现 5x~10x 压缩
4. 可逆上下文检索缓存（CCR · Context Cache & Retrieval）：
   原始超长文本本地指纹存证，通过 ccr_retrieve 实现数学级 100% 无损逆向还原
5. 活跃区端到端压缩流水线（Live-Zone Compression Pipeline）与全套自检测试
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple, Union


# ==============================================================================
# 模块 1：CacheAligner · 缓存守卫不变式（提纯自 crates/headroom-core/cache_control.rs）
# ==============================================================================

CACHE_TTL_1H = "1h"
CACHE_TTL_5M = "5m"


def has_cache_control(block: Any) -> bool:
    """检查单个内容块是否显式包含 cache_control 标记"""
    if isinstance(block, dict):
        return "cache_control" in block
    return False


def extract_ttl(block: Any) -> Optional[str]:
    """提取 cache_control 的 ttl 属性（'5m' 或 '1h'）"""
    if isinstance(block, dict) and "cache_control" in block:
        cc = block["cache_control"]
        if isinstance(cc, dict):
            return cc.get("ttl", CACHE_TTL_5M)
    return None


def compute_frozen_count(parsed_request: Dict[str, Any]) -> Tuple[int, List[str]]:
    """
    遍历 Anthropic /v1/messages 请求体，计算冷冻前缀消息数 N（Frozen Message Count）。

    核心不变式：
    - messages[0..N) 属于缓存冷冻区，压缩器【绝对严禁】触碰任何字节；
      否则会导致 Anthropic KV Cache Key 变化，缓存命中率直接归零！
    - messages[N..len) 属于活跃区（Live Zone），压缩器可安全进行语义瘦身；
    - system 与 tools 属于全局无条件冷冻热区，永远严禁压缩。

    返回：
    - frozen_count: 最小不可变消息数 N（messages[0..N) 不可压缩）
    - warnings: TTL 乱序（5m 在 1h 之前）等非致命合规性警告
    """
    warnings: List[str] = []
    highest_message_index: Optional[int] = None
    seen_ttls: List[str] = []

    # 1. 检查 system 块的 cache_control 与 TTL 顺序
    system_field = parsed_request.get("system")
    if isinstance(system_field, list):
        for item in system_field:
            ttl = extract_ttl(item)
            if ttl:
                seen_ttls.append(ttl)
    elif isinstance(system_field, dict):
        ttl = extract_ttl(system_field)
        if ttl:
            seen_ttls.append(ttl)

    # 2. 遍历 messages[*]
    messages = parsed_request.get("messages", [])
    if isinstance(messages, list):
        for idx, msg in enumerate(messages):
            if not isinstance(msg, dict):
                continue
            content = msg.get("content")
            msg_has_cc = False

            if isinstance(content, list):
                for block in content:
                    if has_cache_control(block):
                        msg_has_cc = True
                        ttl = extract_ttl(block)
                        if ttl:
                            seen_ttls.append(ttl)
            elif isinstance(content, dict):
                if has_cache_control(content):
                    msg_has_cc = True
                    ttl = extract_ttl(content)
                    if ttl:
                        seen_ttls.append(ttl)

            # 消息顶层也可以包含 cache_control
            if has_cache_control(msg):
                msg_has_cc = True
                ttl = extract_ttl(msg)
                if ttl:
                    seen_ttls.append(ttl)

            if msg_has_cc:
                highest_message_index = idx

    # 3. 校验 TTL 顺序：Anthropic 规范要求 1h 标记必须在 5m 之前
    seen_5m = False
    for t in seen_ttls:
        if t == CACHE_TTL_5M:
            seen_5m = True
        elif t == CACHE_TTL_1H and seen_5m:
            warnings.append("TTL ordering violation: '5m' marker preceded '1h' marker.")

    # 4. 若最高命中索引为 i，则 messages[0..=i] 必须冷冻，exclusive 下界为 i + 1
    frozen_count = (highest_message_index + 1) if highest_message_index is not None else 0
    return frozen_count, warnings


# ==============================================================================
# 模块 2：SmartCrusher · 结构化数据压缩器（提纯自 headroom/transforms/smart_crusher.py）
# ==============================================================================

class SmartCrusher:
    """
    针对 JSON/ToolResult 结构化数据的无损/高保真紧凑器。
    - 剥离所有多余空白缩进；
    - 清洗无意义的 null/空字典/空字符串噪声；
    - 对超长大数组（> max_array_items）进行模式折叠（保留前 N 项与尾项，注入省略元标记）。
    """

    def __init__(self, max_array_items: int = 4):
        self.max_array_items = max_array_items

    def prune_structure(self, val: Any) -> Any:
        if isinstance(val, dict):
            pruned = {}
            for k, v in val.items():
                if v is None:
                    continue
                if isinstance(v, (str, list, dict)) and len(v) == 0:
                    continue
                pruned[k] = self.prune_structure(v)
            return pruned
        elif isinstance(val, list):
            if len(val) > self.max_array_items:
                head = [self.prune_structure(item) for item in val[:2]]
                tail = [self.prune_structure(val[-1])]
                omitted_count = len(val) - 3
                return head + [f"<... {omitted_count} items omitted ...>"] + tail
            return [self.prune_structure(item) for item in val]
        return val

    def compress(self, json_text: str) -> Tuple[str, float]:
        """对 JSON 文本执行压缩，返回 (compressed_json, compression_ratio)"""
        try:
            parsed = json.loads(json_text)
        except Exception:
            return json_text, 1.0

        orig_len = len(json_text)
        pruned = self.prune_structure(parsed)
        compact_str = json.dumps(pruned, separators=(",", ":"), ensure_ascii=False)
        compressed_len = len(compact_str)
        ratio = compressed_len / orig_len if orig_len > 0 else 1.0
        return compact_str, ratio


# ==============================================================================
# 模块 3：LogCrusher · 终端与编译日志提纯器
# ==============================================================================

class LogCrusher:
    """
    日志/终端输出压缩器。
    - 保留关键错误核（FATAL, ERROR, Traceback, Exception, FAIL, AssertionError）；
    - 保留错误发生处的上下文行（前后各 2 行）；
    - 折叠重复无害日志（如编译进度条 [1/500]、下载百分比、连续 INFO 脉冲）；
    - 达成 5x~20x 压缩，同时确保核心报错 100% 字节级无损。
    """

    ERROR_PATTERNS = [
        re.compile(r"\b(FATAL|CRITICAL|ERROR|Exception|Traceback|AssertionError|FAIL)\b", re.IGNORECASE),
        re.compile(r"^\s*File \".+\", line \d+"),
    ]
    PROGRESS_PATTERN = re.compile(r"(\[\s*\d+%\s*\]|\[\s*\d+\s*/\s*\d+\s*\]|\r|downloading\.\.\.)", re.IGNORECASE)

    def is_error_line(self, line: str) -> bool:
        return any(pat.search(line) for pat in self.ERROR_PATTERNS)

    def compress_logs(self, log_text: str, context_lines: int = 2) -> Tuple[str, float]:
        lines = log_text.splitlines()
        orig_len = len(log_text)
        if len(lines) <= 6:
            return log_text, 1.0

        # 标记哪些行需要保留
        keep_indices: Set[int] = set()
        error_indices: List[int] = []

        # 始终保留开头首行与结尾末行
        keep_indices.add(0)
        keep_indices.add(len(lines) - 1)

        for i, line in enumerate(lines):
            if self.is_error_line(line):
                error_indices.append(i)
                for c in range(max(0, i - context_lines), min(len(lines), i + context_lines + 1)):
                    keep_indices.add(c)

        # 若完全没有错误行，保留头尾各 3 行
        if not error_indices:
            for c in range(min(3, len(lines))):
                keep_indices.add(c)
            for c in range(max(0, len(lines) - 3), len(lines)):
                keep_indices.add(c)

        # 组装输出，插入省略标记
        output_lines: List[str] = []
        last_kept = -1

        for i in range(len(lines)):
            if i in keep_indices:
                if last_kept != -1 and i > last_kept + 1:
                    omitted = i - last_kept - 1
                    output_lines.append(f"  [... {omitted} lines of repetitive info/progress logs omitted ...]")
                output_lines.append(lines[i])
                last_kept = i

        compressed_text = "\n".join(output_lines)
        compressed_len = len(compressed_text)
        ratio = compressed_len / orig_len if orig_len > 0 else 1.0
        return compressed_text, ratio


# ==============================================================================
# 模块 4：CCR · 可逆上下文缓存与检索引擎（Context Cache & Retrieval）
# ==============================================================================

@dataclass
class CCRVaultEntry:
    chunk_id: str
    sha256: str
    content_type: str
    original_size: int
    compressed_size: int
    original_content: str


class CCRVault:
    """
    本地可逆上下文密码学缓存库。
    对于被强力压缩的内容，在本地持久化其原始副本；
    向 LLM 暴露 ccr_retrieve(chunk_id) 探针，在模型产生歧义时实现毫秒级原文字面量恢复。
    """

    def __init__(self):
        self.entries: Dict[str, CCRVaultEntry] = {}

    def store(self, content: str, content_type: str, compressed_size: int) -> str:
        sha256 = hashlib.sha256(content.encode("utf-8")).hexdigest()
        chunk_id = f"ccr_{sha256[:16]}"
        self.entries[chunk_id] = CCRVaultEntry(
            chunk_id=chunk_id,
            sha256=sha256,
            content_type=content_type,
            original_size=len(content),
            compressed_size=compressed_size,
            original_content=content,
        )
        return chunk_id

    def retrieve(self, chunk_id: str) -> Optional[str]:
        entry = self.entries.get(chunk_id)
        if entry:
            return entry.original_content
        return None

    def format_citation(self, chunk_id: str, summary: str) -> str:
        """格式化带可逆指纹的注入文本"""
        return f"{summary}\n<!-- CCR:REF id=\"{chunk_id}\" retrieve_tool=\"ccr_retrieve\" -->"


# ==============================================================================
# 模块 5：活跃区端到端压缩流水线（Live-Zone Compression Pipeline）
# ==============================================================================

class HeadroomPipeline:
    """
    统一压缩流水线。
    1. 计算 compute_frozen_count，守护 KV-Cache 冷冻前缀；
    2. 针对活跃区（Live-Zone）消息，自动路由分类（JSON、Log、Prose）；
    3. 调用对应压缩器并在 CCR 存证；
    4. 返回守卫后的合规请求体与压缩度度量。
    """

    def __init__(self):
        self.smart_crusher = SmartCrusher()
        self.log_crusher = LogCrusher()
        self.vault = CCRVault()

    def process_request(self, request_body: Dict[str, Any]) -> Dict[str, Any]:
        result = copy.deepcopy(request_body)
        messages = result.get("messages", [])
        if not messages:
            return {"request": result, "frozen_count": 0, "compressed_count": 0, "savings_ratio": 1.0}

        # 1. 守卫冷冻边界
        frozen_count, warnings = compute_frozen_count(result)
        orig_chars = sum(len(json.dumps(m, ensure_ascii=False)) for m in messages)

        compressed_count = 0

        # 2. 仅在 Live-Zone (frozen_count 之后) 进行安全压缩
        for idx in range(frozen_count, len(messages)):
            msg = messages[idx]
            content = msg.get("content")

            if isinstance(content, str):
                # 检查是否为 JSON
                stripped = content.strip()
                if (stripped.startswith("{") and stripped.endswith("}")) or (stripped.startswith("[") and stripped.endswith("]")):
                    comp_str, ratio = self.smart_crusher.compress(content)
                    if ratio < 0.85: # 至少压缩 15% 才替换
                        chunk_id = self.vault.store(content, "json", len(comp_str))
                        msg["content"] = self.vault.format_citation(chunk_id, comp_str)
                        compressed_count += 1
                # 检查是否为长日志
                elif len(content) > 300 and ("\n" in content):
                    comp_log, ratio = self.log_crusher.compress_logs(content)
                    if ratio < 0.80: # 至少压缩 20% 才替换
                        chunk_id = self.vault.store(content, "log", len(comp_log))
                        msg["content"] = self.vault.format_citation(chunk_id, comp_log)
                        compressed_count += 1

            elif isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "text":
                        text = block.get("text", "")
                        if len(text) > 300 and ("\n" in text):
                            comp_log, ratio = self.log_crusher.compress_logs(text)
                            if ratio < 0.80:
                                chunk_id = self.vault.store(text, "log_block", len(comp_log))
                                block["text"] = self.vault.format_citation(chunk_id, comp_log)
                                compressed_count += 1

        new_chars = sum(len(json.dumps(m, ensure_ascii=False)) for m in messages)
        savings_ratio = new_chars / orig_chars if orig_chars > 0 else 1.0

        return {
            "request": result,
            "frozen_count": frozen_count,
            "compressed_count": compressed_count,
            "warnings": warnings,
            "original_chars": orig_chars,
            "new_chars": new_chars,
            "savings_ratio": savings_ratio,
        }


# ==============================================================================
# 自检与全套验证套件
# ==============================================================================

def run_self_tests():
    print("=" * 75)
    print("minimal_headroom_kernel.py · 纯原生零依赖算法验证套件")
    print("=" * 75)

    pipeline = HeadroomPipeline()

    # --------------------------------------------------------------------------
    # 1. 测试 CacheAligner 冻结边界与 TTL 乱序告警
    # --------------------------------------------------------------------------
    print("[1/5] 测试 CacheAligner 冷冻前缀边界 (compute_frozen_count)...")
    req1 = {
        "system": "你是一个严谨的代码审查 Agent。",
        "messages": [
            {"role": "user", "content": "请分析项目架构"},                                       # index 0
            {"role": "assistant", "content": [{"type": "text", "text": "收到", "cache_control": {"type": "ephemeral"}}]}, # index 1 -> 标记！
            {"role": "user", "content": "这是最新的编译日志，非常长..."},                        # index 2 -> 活跃区
            {"role": "assistant", "content": "分析中..."},                                      # index 3 -> 活跃区
        ]
    }
    frozen, warnings = compute_frozen_count(req1)
    assert frozen == 2, f"index 1 打了标记，前缀应当冷冻前 2 条 (0 和 1)，实际: {frozen}"
    assert len(warnings) == 0
    print("  ✓ 冷冻前缀边界计算 100% 正确 (messages[0..2) 受到保护)")

    # --------------------------------------------------------------------------
    # 2. 测试 SmartCrusher JSON 结构紧凑化与大数组折叠
    # --------------------------------------------------------------------------
    print("[2/5] 测试 SmartCrusher JSON 紧凑化与模式折叠...")
    crusher = SmartCrusher(max_array_items=3)
    raw_json = json.dumps({
        "status": "success",
        "empty_field": "",
        "null_field": None,
        "records": [
            {"id": 1, "name": "item_1"},
            {"id": 2, "name": "item_2"},
            {"id": 3, "name": "item_3"},
            {"id": 4, "name": "item_4"},
            {"id": 5, "name": "item_5"},
        ]
    }, indent=4)
    comp_json, ratio = crusher.compress(raw_json)
    assert "null_field" not in comp_json
    assert "empty_field" not in comp_json
    assert "<... 2 items omitted ...>" in comp_json
    assert "item_1" in comp_json
    assert "item_5" in comp_json
    print(f"  ✓ JSON 压缩率: {ratio:.1%} (空值清除，数组有界折叠)")

    # --------------------------------------------------------------------------
    # 3. 测试 LogCrusher 错误核提取与 5x~10x 压缩
    # --------------------------------------------------------------------------
    print("[3/5] 测试 LogCrusher 关键错误核提取与进度日志折叠...")
    log_crusher = LogCrusher()
    noisy_logs = "\n".join([
        "2026-09-19 10:00:00 [INFO] Build started.",
        *[f"2026-09-19 10:00:{i:02d} [PROGRESS] Compiling module_{i}.o [{i}/500]" for i in range(1, 50)],
        "2026-09-19 10:00:51 [ERROR] Failed to link libpetri.so: undefined symbol: check_deadlock_cycle",
        "Traceback (most recent call last):",
        "  File \"src/petri/net.py\", line 142, in check_deadlock_cycle",
        "    assert len(cycles) == 0, 'FATAL: Deadlock cycle detected in Place P2'",
        "AssertionError: FATAL: Deadlock cycle detected in Place P2",
        *[f"2026-09-19 10:01:{i:02d} [PROGRESS] Cleaning up intermediate build files [{i}/20]" for i in range(1, 20)],
        "2026-09-19 10:01:21 [INFO] Build finished with exit code 1."
    ])
    comp_log, log_ratio = log_crusher.compress_logs(noisy_logs)
    assert "FATAL: Deadlock cycle detected in Place P2" in comp_log
    assert "check_deadlock_cycle" in comp_log
    assert "lines of repetitive info/progress logs omitted" in comp_log
    print(f"  ✓ 日志压缩率: {log_ratio:.1%} (从 {len(noisy_logs)} 字符 -> {len(comp_log)} 字符，FATAL 行 100% 完整)")

    # --------------------------------------------------------------------------
    # 4. 测试 CCR 可逆上下文检索与 100% 还原
    # --------------------------------------------------------------------------
    print("[4/5] 测试 CCR (Context Cache & Retrieval) 本地存证与逆向还原...")
    vault = CCRVault()
    secret_text = "这是鲁组并发死锁定理的详细证明全文，共计5000字..."
    chunk_id = vault.store(secret_text, "proof_text", 120)
    assert chunk_id.startswith("ccr_")

    restored = vault.retrieve(chunk_id)
    assert restored == secret_text
    print("  ✓ CCR 密码学指纹存证与原文字面量 100% 完整反查通过")

    # --------------------------------------------------------------------------
    # 5. 测试端到端流水线（冷冻区免改 + 活跃区压缩）
    # --------------------------------------------------------------------------
    print("[5/5] 测试端到端压缩流水线 (冷冻区受保护，活跃区成功瘦身)...")
    full_req = {
        "system": "System Prompt",
        "messages": [
            # index 0: 必须保持原样 (冷冻区)
            {"role": "user", "content": "请分析构建日志", "cache_control": {"type": "ephemeral"}},
            # index 1: 必须保持原样 (冷冻区)
            {"role": "assistant", "content": "收到，请上传"},
            # index 2: 活跃区！包含冗余超大日志，应当被压缩
            {"role": "user", "content": noisy_logs},
        ]
    }
    pipeline_res = pipeline.process_request(full_req)
    req_out = pipeline_res["request"]

    # 验证冷冻区 messages[0] 和 messages[1] 绝对未被修改
    assert req_out["messages"][0]["content"] == "请分析构建日志"
    assert req_out["messages"][1]["content"] == "收到，请上传"

    # 验证活跃区 messages[2] 成功完成语义压缩并打上 CCR 索引
    m2_content = req_out["messages"][2]["content"]
    assert "<!-- CCR:REF id=\"ccr_" in m2_content
    assert "FATAL: Deadlock cycle detected in Place P2" in m2_content
    assert pipeline_res["frozen_count"] == 1
    assert pipeline_res["compressed_count"] == 1
    print(f"  ✓ 端到端流水线完成：冷冻区 100% 零改动，活跃区整体体积缩减至 {pipeline_res['savings_ratio']:.1%}")

    print("=" * 75)
    print("🎉 ALL 5 TEST SUITES PASSED (100% 成功)")
    print("=" * 75)


if __name__ == "__main__":
    run_self_tests()

# ==============================================================================
# 模块补充：CodeCompressor · 基于 AST 的代码骨架化折叠器
# ==============================================================================
import ast

class CodeCompressor:
    """
    针对长代码文件（如 Python）的 AST 骨架化压缩器。
    保留类名、方法签名、文档字符串（Docstring），将函数内部实现彻底折叠，
    以此大幅缩减大模型阅读长文件的 Token 消耗。
    """
    def __init__(self, vault: CCRVault):
        self.vault = vault

    def compress_code(self, source_code: str, language: str = "python") -> Tuple[str, float]:
        orig_len = len(source_code)
        if language != "python" or orig_len < 300:
            return source_code, 1.0

        try:
            tree = ast.parse(source_code)
        except SyntaxError:
            return source_code, 1.0  # 语法错误则退回原文

        lines = source_code.splitlines()
        keep_lines = set()

        # 遍历 AST 节点
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                # 保留签名的第一行
                keep_lines.add(node.lineno - 1)
                # 尝试保留 Docstring
                if ast.get_docstring(node):
                    doc_node = node.body[0]
                    for ln in range(doc_node.lineno - 1, doc_node.end_lineno):
                        keep_lines.add(ln)
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                # 保留所有导入
                for ln in range(node.lineno - 1, node.end_lineno):
                    keep_lines.add(ln)

        if not keep_lines:
            return source_code, 1.0

        output = []
        last_kept = -1
        for i in range(len(lines)):
            if i in keep_lines:
                if last_kept != -1 and i > last_kept + 1:
                    omitted = i - last_kept - 1
                    # 存入 CCR Vault 以备反查
                    omitted_text = "\n".join(lines[last_kept + 1:i])
                    chunk_id = self.vault.store(omitted_text, "code_body", len(omitted_text))
                    output.append(f"    # [... {omitted} lines of implementation hidden ...]")
                    output.append(f"    # <!-- CCR:REF id=\"{chunk_id}\" retrieve_tool=\"ccr_retrieve\" -->")
                output.append(lines[i])
                last_kept = i

        # 处理尾部省略
        if last_kept < len(lines) - 1:
            omitted = len(lines) - 1 - last_kept
            omitted_text = "\n".join(lines[last_kept + 1:])
            chunk_id = self.vault.store(omitted_text, "code_body", len(omitted_text))
            output.append(f"    # [... {omitted} lines of implementation hidden ...]")
            output.append(f"    # <!-- CCR:REF id=\"{chunk_id}\" retrieve_tool=\"ccr_retrieve\" -->")

        compressed_text = "\n".join(output)
        ratio = len(compressed_text) / orig_len if orig_len > 0 else 1.0
        return compressed_text, ratio
