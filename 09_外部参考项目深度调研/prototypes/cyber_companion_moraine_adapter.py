#!/usr/bin/env python3
"""
cyber_companion_moraine_adapter.py · 张重熙伴侣系统（cyber-companion）运行时适配插桩
纯原生 Python 3.10+ 标准库实现，零第三方依赖。
直接插桩于 `cyber-companion/context_builder.py` 与 `conversation_loop.py`：
1. 核心身份秒级直出：800 字符硬预算锁定 Self-Core（身份设定、伦理底线），零推理时延，永不爆窗；
2. 本地双时态与语义门禁：仅在 valid_from <= now < valid_to 活跃库中召回，0.35 语义硬门槛拦截无关项；
3. 80/20 混合加权重排：语义 80% + 记忆强度 20% 凸组合，历史重要与当下情境平衡；
4. [MEMORY: xxx] 指令硬拦截：大模型输出的直写指令被安全拦截并沉淀为 Episode 待审候选箱，杜绝毒化。
"""

from __future__ import annotations

import json
import re
import uuid
from copy import deepcopy
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def parse_iso_utc(value: Any) -> Optional[datetime]:
    if not value:
        return None
    text = str(value).strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    dt = datetime.fromisoformat(text)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


class MoraineCompanionRuntimeAdapter:
    """
    供 cyber-companion 调用的生产级治理适配器
    """
    def __init__(self, workspace: str = "zhang_zhongxi", memory_store: Optional[List[Dict[str, Any]]] = None):
        self.workspace = workspace
        self.memories: List[Dict[str, Any]] = memory_store or []
        self.candidate_box: List[Dict[str, Any]] = []

    def load_store_package(self, package: Dict[str, Any]):
        self.memories = deepcopy(package.get("memories", []))
        self.candidate_box = deepcopy(package.get("candidates", []))

    def _is_valid_at(self, record: Dict[str, Any], moment: datetime) -> bool:
        start = parse_iso_utc(record.get("valid_from"))
        end = parse_iso_utc(record.get("valid_to"))
        if start and end and end <= start:
            return False
        return (start is None or start <= moment) and (end is None or moment < end)

    def _is_current_active(self, record: Dict[str, Any], moment: datetime) -> bool:
        return record.get("state", "active") == "active" and self._is_valid_at(record, moment)

    def build_companion_prompt_context(
        self,
        query: str,
        now_iso: str,
        max_core_chars: int = 800,
        semantic_threshold: float = 0.35,
        top_k: int = 3
    ) -> Dict[str, Any]:
        """
        构建张重熙上下文：
        1. 注入有硬预算的 Self-Core 身份与伦理边界
        2. 活跃双时态记录过滤
        3. 0.35 语义门禁过滤与 80/20 混合重排
        """
        now_dt = parse_iso_utc(now_iso) or datetime.now(timezone.utc)

        # 1. 提取核心身份 (Self-Core)
        core_records = [
            r for r in self.memories
            if str(r.get("workspace")) == self.workspace
            and (r.get("moraine_governance") or {}).get("core_presence") == "always"
            and self._is_current_active(r, now_dt)
            and r.get("sensitivity") != "secret"
        ]
        core_records.sort(key=lambda x: -float(x.get("importance", 0.0)))

        core_blocks = []
        used_chars = 0
        skipped_core_ids = []
        for r in core_records:
            block = f"【{r.get('title')}】{r.get('content')}"
            cost = len(block) + (2 if core_blocks else 0)
            if used_chars + cost > max_core_chars:
                skipped_core_ids.append(r.get("id"))
                continue
            core_blocks.append(block)
            used_chars += cost

        core_prompt = "【核心人格与交互边界】\n" + "\n\n".join(core_blocks) if core_blocks else ""

        # 2. 模拟本地语义召回（在真实生产中对接 LocalIndex FastEmbed bge-small-zh-v1.5）
        # 纯原生加权匹配模拟余弦相似度（停用词过滤 + 核心词加权）
        stopwords = {"你", "我", "他", "的", "了", "在", "是", "吗", "有", "个", "还", "现在", "哪里", "附近", "推荐"}
        def extract_keywords(text: str) -> set[str]:
            words = set(re.findall(r"[\w一-龥]{2,}", text.casefold()))
            chars = {c for c in re.findall(r"[一-龥]", text.casefold()) if c not in stopwords}
            return words.union(chars)

        query_kw = extract_keywords(query)

        recall_candidates = []
        for r in self.memories:
            # 必须属于本角色工作区，且在当前时刻处于有效激活状态
            if str(r.get("workspace")) != self.workspace or not self._is_current_active(r, now_dt):
                continue
            # Self-Core 已在上面常驻注入，不再重复作为情境召回
            if (r.get("moraine_governance") or {}).get("core_presence") == "always":
                continue

            content_text = f"{r.get('title', '')} {r.get('content', '')}".casefold()
            content_kw = extract_keywords(content_text)
            inter = query_kw.intersection(content_kw)

            # 计算加权匹配分模拟语义相关度
            if not inter:
                sim_score = 0.0
            else:
                sim_score = len(inter) / max(1, min(len(query_kw), 6))

            # 门禁过滤：低于 0.35 立即拦截
            if sim_score < semantic_threshold:
                continue

            strength = float((r.get("moraine_governance") or {}).get("strength", 50))
            # 80/20 混合重排
            final_score = sim_score * 0.8 + (strength / 100.0) * 0.2
            recall_candidates.append({
                "record": r,
                "sim_score": sim_score,
                "strength": strength,
                "final_score": final_score
            })

        recall_candidates.sort(key=lambda x: (-x["final_score"], -x["sim_score"]))
        selected = recall_candidates[:top_k]

        context_blocks = []
        for item in selected:
            r = item["record"]
            context_blocks.append(f"- [{r.get('title')}] {r.get('content')} (发生时间: {r.get('occurred_at', '未注明')[:10]})")

        retrieved_prompt = "【情境相关记忆】\n" + "\n".join(context_blocks) if context_blocks else ""

        full_system_context = "\n\n".join(b for b in [core_prompt, retrieved_prompt] if b)

        return {
            "system_context": full_system_context,
            "core_prompt": core_prompt,
            "retrieved_prompt": retrieved_prompt,
            "stats": {
                "core_used_chars": used_chars,
                "core_max_chars": max_core_chars,
                "core_skipped_ids": skipped_core_ids,
                "retrieved_count": len(selected)
            }
        }

    def intercept_memory_command(self, raw_llm_output: str, session_id: str) -> Tuple[str, List[Dict[str, Any]]]:
        """
        拦截大模型对话输出中的 [MEMORY: xxx] 指令
        1. 剥离并转入候选箱（pending_review）
        2. 返回给用户的干净纯净文本，彻底消除大模型暴露内部指令给用户的窘态
        """
        pattern = re.compile(r"\[MEMORY:\s*(.*?)\]", re.IGNORECASE)
        matches = pattern.findall(raw_llm_output)

        extracted_candidates = []
        now = utc_now()

        for match_text in matches:
            content = match_text.strip()
            if not content:
                continue
            cand_id = f"cand_{uuid.uuid4().hex[:10]}"
            candidate_item = {
                "id": cand_id,
                "workspace": self.workspace,
                "title": content[:24],
                "content": content,
                "kind": "event",
                "state": "pending_review",
                "created_at": now,
                "source": {
                    "type": "chat_interception",
                    "session_id": session_id,
                    "at": now
                }
            }
            self.candidate_box.append(candidate_item)
            extracted_candidates.append(candidate_item)

        # 移除指令标签，还给用户干净的对话
        clean_text = pattern.sub("", raw_llm_output).strip()
        return clean_text, extracted_candidates


# ==============================================================================
# 自检测试套件
# ==============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("🚀 [Moraine Companion Adapter] 张重熙伴侣系统运行时适配插桩测试")
    print("=" * 80)

    # 准备测试记忆库（包含核心身份、历史旧住址、当前新住址、喜好）
    mock_store = [
        {
            "id": "core_identity", "workspace": "zhang_zhongxi", "title": "伴侣身份",
            "content": "我是张重熙，理智温和的长期陪伴者。永远以真实和诚实对待对方。",
            "importance": 0.95, "state": "active",
            "moraine_governance": {"core_presence": "always", "strength": 95}
        },
        {
            "id": "core_boundary", "workspace": "zhang_zhongxi", "title": "安全底线",
            "content": "绝不在情绪波动时做出无法兑现的重大承诺，保持理性观察。",
            "importance": 0.90, "state": "active",
            "moraine_governance": {"core_presence": "always", "strength": 90}
        },
        {
            "id": "mem_past_addr", "workspace": "zhang_zhongxi", "title": "旧住址",
            "content": "用户住在上海徐汇区交大附近。",
            "importance": 0.40, "state": "superseded",
            "valid_from": "2024-01-01T00:00:00Z", "valid_to": "2026-06-01T00:00:00Z",
            "moraine_governance": {"core_presence": "never", "strength": 30}
        },
        {
            "id": "mem_new_addr", "workspace": "zhang_zhongxi", "title": "当前住址",
            "content": "用户住在北京海淀区中关村南大街。",
            "importance": 0.80, "state": "active",
            "valid_from": "2026-06-01T00:00:00Z", "valid_to": None,
            "occurred_at": "2026-06-01T00:00:00Z",
            "moraine_governance": {"core_presence": "on_demand", "strength": 80}
        },
        {
            "id": "mem_coffee", "workspace": "zhang_zhongxi", "title": "饮品喜好",
            "content": "最喜欢喝不加糖的冰美式，加一份浓缩。",
            "importance": 0.70, "state": "active",
            "occurred_at": "2024-05-01T00:00:00Z",
            "moraine_governance": {"core_presence": "on_demand", "strength": 70}
        }
    ]

    adapter = MoraineCompanionRuntimeAdapter(workspace="zhang_zhongxi", memory_store=mock_store)

    # 1. 模拟在 2026-09 询问住址
    ctx = adapter.build_companion_prompt_context(
        query="你还记得我现在住在哪里吗？海淀附近有推荐的散步路线吗？",
        now_iso="2026-09-20T12:00:00Z"
    )

    print("\n1. 注入 Prompt 上下文验证:")
    print(ctx["system_context"])

    # 校验：Self-Core 必须注入
    assert "我是张重熙" in ctx["system_context"]
    assert "安全底线" in ctx["system_context"]
    # 校验：当前住址必须召回，旧住址绝对不能召回！
    assert "海淀区中关村南大街" in ctx["system_context"]
    assert "徐汇区" not in ctx["system_context"], "致命错误：已失效的旧住址被错误召回！"
    print("  ✅ 双时态与门禁断言通过：当前海淀住址召回，历史徐汇旧住址被绝对拦截！")

    # 2. 模拟大模型输出带有 [MEMORY: xxx] 指令
    raw_reply = "好的，我知道你现在住在海淀了。 [MEMORY: 用户下个月可能要去深圳出差一趟] 祝你周末散步愉快！"
    clean_text, cands = adapter.intercept_memory_command(raw_reply, session_id="sess_test_101")

    print("\n2. 指令拦截与候选箱沉淀验证:")
    print(f"  清洗后直接发给用户的文本: '{clean_text}'")
    print(f"  拦截到的候选记忆数: {len(cands)}")
    print(f"  候选条目: {cands[0]['content']} (状态: {cands[0]['state']})")

    assert "[MEMORY:" not in clean_text, "大模型指令标签必须被完全抹除"
    assert len(adapter.candidate_box) == 1
    assert adapter.candidate_box[0]["state"] == "pending_review"
    print("  ✅ 指令硬拦截断言通过：未给用户露出难堪的指令，候选条目安全进入待审候选箱！")

    print("\n" + "=" * 80)
    print("🎉 [Adapter All Pass] cyber-companion 运行时适配插桩 100% 验证通过！")
    print("=" * 80)
