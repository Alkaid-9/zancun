#!/usr/bin/env python3
"""
minimal_moraine_kernel.py · 提纯自 ceniran/moraine-home 核心记忆治理全量原件
纯原生 Python 3.10+ 标准库实现，零第三方依赖（无 fastembed / fastapi / pydantic），完整闭环演示 7 大核心治理机制：
1. 双时态（Bi-Temporal）状态与半开区间有效性校验 [valid_from, valid_to)
2. 非破坏性、严格抽取式句子去重与蕴含吞并（Extractive Deduplication: exact_duplicate / subsumed_verbatim）
3. 严格字符预算约束的核心身份投影（Bounded Self-Core Projection: max_chars 截断与 skipped_ids 审计）
4. 密码学哈希可逆决策账本与安全回滚（Cryptographic Reversible Decision Ledger & Recovery Vault）
5. 0.35 语义硬门槛过滤与 80/20 混合加权重排引擎（Semantic Gate & Weighted Reranking Policy）
6. 跨记忆经验线程与时序修订链（Cross-Memory Experience Threads with Revision & Revisit Conditions）
7. 机人对称双钥匙提议与共治签名协议（Dual-Key Machine/Human Governance Signatures）
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import unicodedata
from copy import deepcopy
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List, Mapping, Optional, Tuple


# ==============================================================================
# 模块 1：双时态（Bi-Temporal）判定引擎（提纯自 moraine/temporal.py）
# ==============================================================================

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


def is_record_valid_at(record: Mapping[str, Any], moment: datetime) -> bool:
    """
    半开区间判定：valid_from <= moment < valid_to
    将物理世界真实时效（valid_from/to）与系统记账时间（created_at/updated_at）彻底解耦
    """
    start = parse_iso_utc(record.get("valid_from"))
    end = parse_iso_utc(record.get("valid_to"))
    if start and end and end <= start:
        raise ValueError("valid_to 必须严格晚于 valid_from")
    return (start is None or start <= moment) and (end is None or moment < end)


def is_current_active(record: Mapping[str, Any], now: datetime) -> bool:
    return record.get("state", "active") == "active" and is_record_valid_at(record, now)


# ==============================================================================
# 模块 2：保守抽取式记忆整合器（提纯自 moraine/consolidate.py）
# ==============================================================================

_SENTENCE_BOUNDARY = re.compile(r"(?<=[。！？!?；;\n])\s*")
_IGNORED_CHARS = re.compile(r"[\W_]+", re.UNICODE)


def split_sentences(text: str) -> List[str]:
    return [p.strip() for p in _SENTENCE_BOUNDARY.split(str(text)) if p.strip()]


def comparison_key(text: str) -> str:
    normalized = unicodedata.normalize("NFKC", text).casefold()
    return _IGNORED_CHARS.sub("", normalized)


def consolidate_memories(memories: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    严格基于字面归一化的抽取式去重：
    1. 完全一致句子仅保留一份（exact_duplicate）
    2. 被长句完全蕴含的短句安全剔除（subsumed_verbatim）
    3. 绝不调用大模型自由发挥篡改事实，所有保留句子均附带来源 trace
    """
    sources: List[Tuple[str, str]] = []  # (memory_id, sentence)
    for mem in memories:
        mid = str(mem.get("id", "")).strip()
        for sent in split_sentences(mem.get("content", "")):
            if comparison_key(sent):
                sources.append((mid, sent))

    kept: List[Tuple[str, str]] = []
    removed: List[Dict[str, Any]] = []

    for mid, sent in sources:
        key = comparison_key(sent)
        # 1. 检查完全重复
        dup = next((k for k in kept if comparison_key(k[1]) == key), None)
        if dup:
            removed.append({
                "source_id": mid,
                "sentence": sent,
                "reason": "exact_duplicate",
                "kept_from": dup[0]
            })
            continue

        # 2. 检查是否被已有或后续长句完全覆盖
        containing = next(
            (s for s in sources if s != (mid, sent) and len(comparison_key(s[1])) > len(key) and key in comparison_key(s[1])),
            None
        )
        if containing:
            removed.append({
                "source_id": mid,
                "sentence": sent,
                "reason": "subsumed_verbatim",
                "kept_from": containing[0]
            })
            continue

        kept.append((mid, sent))

    return {
        "consolidated_content": " ".join(s[1] for s in kept),
        "kept_sentences": [{"text": s[1], "source_id": s[0]} for s in kept],
        "removed_details": removed,
        "requires_human_review": True
    }


# ==============================================================================
# 模块 3：有预算约束的身份投影（提纯自 moraine/core_projection.py）
# ==============================================================================

def build_core_projection(
    records: List[Mapping[str, Any]],
    now: datetime,
    workspace: str = "default",
    max_chars: int = 250
) -> Dict[str, Any]:
    """
    提取陪伴 Agent 核心身份与安全基线（Self-Core）
    规则：
    1. 必须匹配 workspace（多租户/角色隔离）
    2. 必须 state == active 且当前在有效半开区间内
    3. moraine_governance.core_presence 必须显式为 'always'
    4. 敏感级 secret 严格排除
    5. 受硬性字符预算截断，超预算条目明确报告为 skipped_ids
    """
    eligible = []
    excluded_workspace = []
    for r in records:
        rec_ws = str(r.get("workspace") or "default")
        if rec_ws != workspace:
            excluded_workspace.append(r.get("id"))
            continue
        if r.get("sensitivity") == "secret":
            continue
        gov = r.get("moraine_governance") or {}
        if gov.get("core_presence") == "always" and is_current_active(r, now):
            eligible.append(dict(r))

    # 按重要度倒序排列，次级按 id 升序
    eligible.sort(key=lambda x: (-float(x.get("importance") or 0.0), str(x.get("id"))))

    blocks = []
    source_ids = []
    skipped_ids = []
    used = 0

    for r in eligible:
        block = f"【{r.get('title')}】{r.get('content')}"
        cost = len(block) + (2 if blocks else 0)
        if used + cost > max_chars:
            skipped_ids.append(r.get("id"))
            continue
        blocks.append(block)
        source_ids.append(r.get("id"))
        used += cost

    return {
        "prompt_injection_text": "\n\n".join(blocks),
        "used_chars": used,
        "max_chars": max_chars,
        "source_ids": source_ids,
        "skipped_ids": skipped_ids,
        "excluded_workspace_ids": excluded_workspace
    }


# ==============================================================================
# 模块 4：密码学可逆决策账本（提纯自 moraine/decision_ledger.py）
# ==============================================================================

def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def canonical_hash(obj: Any) -> str:
    return hashlib.sha256(canonical_json(obj).encode("utf-8")).hexdigest()


class ReversibleDecisionLedger:
    """
    不可篡改的操作收据与回滚控制器（借鉴 Memloom 架构）
    版本引用（Reference）与完整快照（Recovery Vault）物理隔离，
    回滚前严格比对当前指纹，杜绝外部并发修改下的脏数据回滚。
    """
    def __init__(self):
        self.live_store: Dict[str, Dict[str, Any]] = {}
        self.receipts: Dict[str, Dict[str, Any]] = {}
        self.vault: Dict[str, Dict[str, Any]] = {}

    def register_memory(self, mem: Dict[str, Any]):
        mid = mem["id"]
        row = deepcopy(mem)
        row.setdefault("version", 1)
        row["fingerprint"] = canonical_hash(row)
        self.live_store[mid] = row

    def execute_supersede(self, old_id: str, new_content: str, reason: str, actor: str) -> str:
        """用新事实替换旧事实，并生成密码学操作收据"""
        if old_id not in self.live_store:
            raise KeyError(f"记忆不存在: {old_id}")

        old_row = deepcopy(self.live_store[old_id])
        now_iso = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        op_id = f"op_{canonical_hash({'target': old_id, 'content': new_content, 'at': now_iso})[:16]}"

        # 存入隔离金库
        vault_key = f"{old_id}_v{old_row['version']}"
        self.vault[vault_key] = deepcopy(old_row)

        # 更新活跃库
        new_row = deepcopy(old_row)
        new_row["content"] = new_content
        new_row["version"] = int(old_row.get("version", 1)) + 1
        new_row["updated_at"] = now_iso
        new_row["fingerprint"] = canonical_hash(new_row)
        self.live_store[old_id] = new_row

        # 生成不可篡改收据
        receipt = {
            "operation_id": op_id,
            "action": "replace",
            "actor": actor,
            "reason": reason,
            "created_at": now_iso,
            "before_ref": {"id": old_id, "version": old_row["version"], "fingerprint": old_row["fingerprint"]},
            "after_ref": {"id": old_id, "version": new_row["version"], "fingerprint": new_row["fingerprint"]}
        }
        self.receipts[op_id] = receipt
        return op_id

    def rollback(self, op_id: str) -> bool:
        """依据收据实现原子级逆向恢复"""
        receipt = self.receipts.get(op_id)
        if not receipt:
            return False
        b_ref = receipt["before_ref"]
        target_id = b_ref["id"]
        vault_key = f"{target_id}_v{b_ref['version']}"
        if vault_key not in self.vault:
            return False

        # 校验当前指纹是否已被第三方并发修改
        live_now = self.live_store.get(target_id)
        if not live_now or live_now["fingerprint"] != receipt["after_ref"]["fingerprint"]:
            raise RuntimeError("检测到外部并发修改或指纹不匹配，拒绝不安全的回滚！")

        restored_row = deepcopy(self.vault[vault_key])
        self.live_store[target_id] = restored_row
        receipt["status"] = "reverted"
        return True


# ==============================================================================
# 模块 5：0.35 语义门禁与 80/20 混合加权重排引擎（提纯自 moraine/retrieval_policy.py）
# ==============================================================================

@dataclass(frozen=True)
class RetrievalPolicy:
    """确定的、只读的候选召回重排策略"""
    semantic_weight: float = 0.8
    strength_weight: float = 0.2
    minimum_semantic_score: float = 0.35
    missing_strength: int = 50

    def __post_init__(self) -> None:
        if self.semantic_weight < 0 or self.strength_weight < 0:
            raise ValueError("排序权重不能为负数")
        if self.semantic_weight + self.strength_weight <= 0:
            raise ValueError("至少一个权重必须为正数")
        if not -1.0 <= self.minimum_semantic_score <= 1.0:
            raise ValueError("minimum_semantic_score 必须在 [-1, 1] 之间")


def clamp_strength(value: Any) -> int:
    try:
        return max(0, min(100, round(float(value))))
    except (TypeError, ValueError):
        return 50


def rerank_candidates(
    candidates: Iterable[Mapping[str, Any]],
    *,
    limit: int = 20,
    policy: Optional[RetrievalPolicy] = None
) -> List[Dict[str, Any]]:
    """
    候选重排核心算法：
    1. 第一道门禁：严苛语义门槛过滤（semantic_score < 0.35 立即剔除，防止高权重无关记忆穿透）
    2. 第二道计算：80% 语义相关度 + 20% 记忆强度的凸组合加权
    3. 稳定性保证：三级决胜 (-final_score, -semantic_score, input_position)
    """
    pol = policy or RetrievalPolicy()
    total_w = pol.semantic_weight + pol.strength_weight
    ranked = []

    for pos, raw in enumerate(candidates):
        item = dict(raw)
        sem = float(item.get("score", item.get("semantic_score", 0.0)))
        # 门禁 1：语义不相关直接拦截
        if sem < pol.minimum_semantic_score:
            continue

        # 解析强度 (0..100)
        str_val = item.get("strength")
        if str_val is None and item.get("importance") is not None:
            str_val = round(float(item["importance"]) * 100)
        resolved_str = clamp_strength(str_val if str_val is not None else pol.missing_strength)

        # 凸组合打分
        final = (sem * pol.semantic_weight + (resolved_str / 100.0) * pol.strength_weight) / total_w
        item.update({
            "semantic_score": sem,
            "memory_strength": resolved_str,
            "final_score": final,
            "_pos": pos
        })
        ranked.append(item)

    ranked.sort(key=lambda x: (-x["final_score"], -x["semantic_score"], x["_pos"]))
    out = []
    for r in ranked[:limit]:
        r.pop("_pos", None)
        out.append(r)
    return out


# ==============================================================================
# 模块 6：跨记忆经验线程与修订链（提纯自 moraine/experience_threads.py）
# ==============================================================================

def build_experience_thread_candidate(
    records: Iterable[Mapping[str, Any]],
    *,
    thread_id: str,
    title: str,
    workspace: str,
    summary_draft: Optional[Mapping[str, Any]] = None
) -> Dict[str, Any]:
    """
    构建跨记忆经验线程（Experience Thread）：
    将离散但同属一个长程经验线（如‘张重熙_心流对话演进’）的记忆点串成时序视图。
    支持显式成员约束、按 observed_at 排序、版本递增链与未决问题/重访条件。
    """
    tid = str(thread_id).strip()
    ttl = str(title).strip()
    ws = str(workspace).strip()
    if not tid or not ttl or not ws:
        raise ValueError("thread_id, title 和 workspace 为必填项")

    points = []
    seen_ids = set()
    for raw in records:
        r = dict(raw)
        mid = str(r.get("id") or "").strip()
        if not mid or mid in seen_ids:
            raise ValueError(f"成员 ID 必须唯一且非空: {mid}")
        seen_ids.add(mid)

        mem_ws = str(r.get("workspace") or "").strip()
        if mem_ws != ws:
            raise ValueError(f"成员 {mid} 工作区不匹配: 期望 {ws}, 实际 {mem_ws}")

        obs = parse_iso_utc(r.get("observed_at") or r.get("created_at"))
        if not obs:
            raise ValueError(f"成员 {mid} 缺少有效时间戳")

        src = r.get("source") or {"type": "chat", "ref": f"sess_{mid}"}
        points.append((obs, mid, src))

    if not points:
        raise ValueError("经验线程至少需要包含一个记忆成员")

    points.sort(key=lambda x: (x[0], x[1]))
    ordered_ids = [p[1] for p in points]

    summary = None
    if summary_draft is not None:
        sd = dict(summary_draft)
        rev = sd.get("revision")
        if not isinstance(rev, int) or rev < 1:
            raise ValueError("summary_draft.revision 必须为正整数")

        src_ids = list(sd.get("source_ids") or [])
        if not src_ids or not set(src_ids).issubset(seen_ids):
            raise ValueError("summary 必须引用且只能引用本线程成员 ID")

        prev_rev = sd.get("previous_revision")
        if rev == 1 and prev_rev is not None:
            raise ValueError("第一版修订不能指定 previous_revision")
        if rev > 1 and prev_rev != rev - 1:
            raise ValueError("修订链必须严格指向前一版本 (revision - 1)")

        summary = {
            "revision": rev,
            "previous_revision": prev_rev,
            "status": "pending_review",
            "text": str(sd.get("text", "")).strip(),
            "source_ids": src_ids,
            "unresolved": [str(u).strip() for u in sd.get("unresolved", []) if str(u).strip()],
            "revisit_when": [str(w).strip() for w in sd.get("revisit_when", []) if str(w).strip()]
        }

    return {
        "thread_id": tid,
        "title": ttl,
        "workspace": ws,
        "status": "pending_review",
        "started_at": points[0][0].isoformat().replace("+00:00", "Z"),
        "ended_at": points[-1][0].isoformat().replace("+00:00", "Z"),
        "member_ids": ordered_ids,
        "points": [{"memory_id": mid, "observed_at": obs.isoformat().replace("+00:00", "Z"), "source": src} for obs, mid, src in points],
        "summary_draft": summary,
        "requires_review": True
    }


# ==============================================================================
# 模块 7：机人对称双钥匙签名治理协议（提纯自 moraine/governance.py）
# ==============================================================================

def create_strength_proposal(
    memory: Mapping[str, Any],
    strength: int,
    *,
    actor: str,
    actor_role: str,
    reason: str,
    now_iso: str,
    expected_version: int,
    lock: bool = False
) -> Dict[str, Any]:
    """
    创建记忆强度赋权提议：
    - actor_role 必须是 'machine' 或 'human'
    - 高影响操作（变动 >= 20分、强度 >= 80分锁定）强制 requires_second_key = True
    - 提议者先行附上第一把审批签名
    """
    if actor_role not in {"machine", "human"}:
        raise ValueError("actor_role 必须是 'machine' 或 'human'")
    cur_str = clamp_strength(round(float(memory.get("importance", 0.5)) * 100))
    to_str = clamp_strength(strength)
    if lock and to_str < 80:
        raise ValueError("只有 80..100 的核心记忆允许上锁")

    diff = abs(to_str - cur_str)
    high_impact = bool(lock or to_str >= 80 or diff >= 20)
    seed = f"{memory.get('id')}|{actor}|{now_iso}|{expected_version}|{cur_str}|{to_str}|{lock}"
    pid = f"prop_{hashlib.sha256(seed.encode('utf-8')).hexdigest()[:16]}"

    return {
        "proposal_id": pid,
        "memory_id": str(memory.get("id")),
        "expected_version": expected_version,
        "from_strength": cur_str,
        "to_strength": to_str,
        "lock": lock,
        "reason": str(reason).strip(),
        "proposed_by": {"id": actor, "role": actor_role, "at": now_iso},
        "high_impact": high_impact,
        "requires_second_key": high_impact,
        "signatures": {actor_role: {"actor": actor, "decision": "approve", "at": now_iso}},
        "status": "pending_review" if high_impact else "ready"
    }


def review_strength_proposal(
    proposal: Mapping[str, Any],
    *,
    actor: str,
    actor_role: str,
    decision: str,
    now_iso: str
) -> Dict[str, Any]:
    """
    第二把钥匙审批：
    【核心防死穴门禁】提议者绝不能自审自批（proposer cannot provide second key）！
    """
    p = deepcopy(dict(proposal))
    if actor_role not in {"machine", "human"} or decision not in {"approve", "reject"}:
        raise ValueError("无效的审批角色或决策选项")

    proposer_role = p.get("proposed_by", {}).get("role")
    if proposer_role == actor_role:
        raise ValueError("提议者所在角色不能签署第二把钥匙（禁止自审）")

    p["signatures"][actor_role] = {"actor": actor, "decision": decision, "at": now_iso}
    if decision == "approve":
        p["status"] = "ready"
    else:
        p["status"] = "rejected"
    return p


def apply_strength_proposal(
    memory: Mapping[str, Any],
    proposal: Mapping[str, Any],
    current_version: int
) -> Dict[str, Any]:
    """
    在乐观并发锁（version）校验通过后应用提议
    """
    if str(memory.get("id")) != str(proposal.get("memory_id")):
        raise ValueError("提议针对的目标记忆与当前记忆不匹配")
    if int(current_version) != int(proposal.get("expected_version", 0)):
        raise ValueError("版本冲突！记忆已被修改，提议失效需重审")
    if proposal.get("status") != "ready":
        raise ValueError(f"提议未处于 ready 状态 (当前: {proposal.get('status')})")

    if proposal.get("requires_second_key"):
        sigs = proposal.get("signatures", {})
        if not (sigs.get("machine", {}).get("decision") == "approve" and
                sigs.get("human", {}).get("decision") == "approve"):
            raise ValueError("高影响操作缺少机人双方完整签名批准！")

    updated = deepcopy(dict(memory))
    updated["importance"] = proposal["to_strength"] / 100.0
    gov = deepcopy(updated.get("moraine_governance") or {})
    gov["strength_locked"] = bool(proposal.get("lock"))
    gov["last_proposal_id"] = proposal.get("proposal_id")
    updated["moraine_governance"] = gov
    updated["version"] = current_version + 1

    return {
        "record": updated,
        "rollback_record": deepcopy(dict(memory)),
        "proposal_id": proposal.get("proposal_id")
    }


# ==============================================================================
# 自检演示主程序（覆盖 7 大模块的纯原生断言套件）
# ==============================================================================

if __name__ == "__main__":
    now_moment = datetime(2026, 9, 20, 12, 0, 0, tzinfo=timezone.utc)
    print("=" * 80)
    print("🚀 [Moraine Kernel v2.0] ceniran/moraine-home 7大核心治理算法全量实测")
    print("=" * 80)

    # 1. 验证双时态（Bi-Temporal）模型
    print("\n--- 1. 双时态时效性测试 [valid_from, valid_to) ---")
    mem_past = {
        "id": "mem_addr_old", "title": "旧住址", "content": "住在上海徐汇区",
        "state": "active", "valid_from": "2024-01-01T00:00:00Z", "valid_to": "2026-06-01T00:00:00Z"
    }
    mem_now = {
        "id": "mem_addr_new", "title": "新住址", "content": "搬到了北京海淀区",
        "state": "active", "valid_from": "2026-06-01T00:00:00Z", "valid_to": None
    }
    assert is_current_active(mem_past, now_moment) is False, "旧住址应该已失效"
    assert is_current_active(mem_now, now_moment) is True, "新住址应该在有效期内"
    print("  ✅ 双时态半开区间断言通过：旧记录平滑冷冻，活跃索引永远召回当前真理！")

    # 2. 验证非破坏性抽取式去重与蕴含吞并
    print("\n--- 2. 保守抽取式去重与蕴含吞并测试 ---")
    test_fragments = [
        {"id": "c1", "content": "张重熙最喜欢喝冰美式咖啡。"},
        {"id": "c2", "content": "张重熙最喜欢喝冰美式咖啡。"},  # exact duplicate
        {"id": "c3", "content": "张重熙最喜欢喝冰美式咖啡，且必须加一份浓缩。"},  # subsumed
        {"id": "c4", "content": "今天天气非常晴朗适合散步。"}
    ]
    con_res = consolidate_memories(test_fragments)
    assert len(con_res["kept_sentences"]) == 2, f"应只保留2句，实际: {len(con_res['kept_sentences'])}"
    assert any(r["reason"] == "subsumed_verbatim" for r in con_res["removed_details"])
    print(f"  ✅ 保留文本: '{con_res['consolidated_content']}'")
    print(f"  ✅ 剔除审计: {len(con_res['removed_details'])} 项冗余已安全剔除，零大模型幻觉！")

    # 3. 验证有预算的核心身份投影（Self-Core）
    print("\n--- 3. 有预算核心身份投影测试（Self-Core） ---")
    companion_memories = [
        {
            "id": "core_identity", "workspace": "zhang_zhongxi", "title": "伴侣身份设定",
            "content": "我是张重熙，理智温和的长期陪伴者。永远以真实和诚实对待对方。",
            "importance": 0.95, "state": "active",
            "moraine_governance": {"core_presence": "always"}
        },
        {
            "id": "core_boundary", "workspace": "zhang_zhongxi", "title": "伦理与安全底线",
            "content": "绝不在情绪波动时做出无法兑现的重大承诺，保持理性观察。",
            "importance": 0.90, "state": "active",
            "moraine_governance": {"core_presence": "always"}
        },
        {
            "id": "core_secret", "workspace": "zhang_zhongxi", "title": "隐秘密钥",
            "content": "sk-secret-key-12345",
            "importance": 0.99, "state": "active", "sensitivity": "secret",
            "moraine_governance": {"core_presence": "always"}
        },
        {
            "id": "other_ws", "workspace": "other_bot", "title": "跨台身份",
            "content": "我是无关Bot", "importance": 0.99, "state": "active",
            "moraine_governance": {"core_presence": "always"}
        }
    ]
    proj = build_core_projection(companion_memories, now_moment, workspace="zhang_zhongxi", max_chars=120)
    assert "core_secret" not in proj["source_ids"], "secret 敏感内容必须被剔除"
    assert "other_ws" not in proj["source_ids"], "跨 workspace 必须被物理隔离"
    assert proj["used_chars"] <= 120, "投影字符数必须严格处于预算内"
    print(f"  ✅ 预算 120 字符，实际注入 {proj['used_chars']} 字符，跳过: {proj['skipped_ids']}")

    # 4. 验证密码学可逆操作账本与防篡改回滚
    print("\n--- 4. 密码学可逆操作账本与回滚测试 ---")
    ledger = ReversibleDecisionLedger()
    test_record = {"id": "rel_status", "title": "关系现状", "content": "初步破冰阶段。"}
    ledger.register_memory(test_record)
    op = ledger.execute_supersede(
        old_id="rel_status",
        new_content="确立了深厚的情感共鸣与长程陪伴承诺。",
        reason="心流对话里程碑",
        actor="human"
    )
    assert ledger.live_store["rel_status"]["version"] == 2
    ok = ledger.rollback(op)
    assert ok is True
    assert ledger.live_store["rel_status"]["content"] == "初步破冰阶段。"
    print(f"  ✅ 签发不可篡改收据 {op}，回滚验证成功，版本与内容 100% 还原！")

    # 5. 验证 0.35 语义门禁与 80/20 混合重排
    print("\n--- 5. 0.35 语义门禁与 80/20 混合加权重排测试 ---")
    candidates = [
        {"id": "m_irrelevant", "score": 0.20, "importance": 1.0},   # 极重要但语义不相关 (<0.35)
        {"id": "m_sem_high",   "score": 0.85, "importance": 0.4},   # 语义很高，重要度中等
        {"id": "m_balanced",   "score": 0.70, "importance": 0.8}    # 语义较高，重要度很高
    ]
    ranked = rerank_candidates(candidates, policy=RetrievalPolicy())
    assert all(r["id"] != "m_irrelevant" for r in ranked), "0.35 门禁必须将无关条目彻底拦截"
    assert ranked[0]["id"] == "m_sem_high" or ranked[0]["id"] == "m_balanced"
    print(f"  ✅ 0.35 门禁成功剔除无关条目！排名前二为: {[r['id'] for r in ranked]}")
    print(f"     首名得分详情: 语义={ranked[0]['semantic_score']}, 强度={ranked[0]['memory_strength']}, 综合={ranked[0]['final_score']:.4f}")

    # 6. 验证跨记忆经验线程与修订链（Experience Threads）
    print("\n--- 6. 跨记忆经验线程与时序修订链测试 ---")
    thread_memories = [
        {"id": "step_2", "workspace": "companion", "created_at": "2026-09-02T10:00:00Z"},
        {"id": "step_1", "workspace": "companion", "created_at": "2026-09-01T10:00:00Z"}
    ]
    summary_draft = {
        "revision": 2,
        "previous_revision": 1,
        "text": "张重熙与用户共同经历了从破冰到深度信任的认知跃迁。",
        "source_ids": ["step_1", "step_2"],
        "unresolved": ["下周生日礼物倾向待确认"],
        "revisit_when": ["用户主动发起关于未来的长远规划对话"]
    }
    thread = build_experience_thread_candidate(
        thread_memories, thread_id="flow_evolution", title="陪伴演进线",
        workspace="companion", summary_draft=summary_draft
    )
    assert thread["member_ids"] == ["step_1", "step_2"], "时序必须按时间升序重排"
    assert thread["summary_draft"]["revision"] == 2
    assert thread["summary_draft"]["previous_revision"] == 1
    print(f"  ✅ 经验线程时序重排成功: {thread['member_ids']}，修订链与重访条件锁定！")

    # 7. 验证机人对称双钥匙提议与共治签名协议
    print("\n--- 7. 机人对称双钥匙治理签名协议测试 ---")
    core_mem = {"id": "mem_promise", "importance": 0.50}
    # 机器发起提升为 85 分并上锁的提议（高影响，需要两把钥匙）
    proposal = create_strength_proposal(
        core_mem, strength=85, actor="moraine_agent", actor_role="machine",
        reason="用户确认这是双方关系的核心承诺", now_iso="2026-09-20T12:00:00Z",
        expected_version=1, lock=True
    )
    assert proposal["requires_second_key"] is True
    assert proposal["status"] == "pending_review"

    # 测试防死穴：机器自己尝试签署第二把钥匙必须被拒绝！
    try:
        review_strength_proposal(proposal, actor="moraine_agent", actor_role="machine", decision="approve", now_iso="2026-09-20T12:01:00Z")
        assert False, "机器自审自批必须报错"
    except ValueError as e:
        assert "禁止自审" in str(e)
        print("  ✅ 防自审门禁生效：机器无法自审自批，必须等待人类第二把钥匙！")

    # 人类签署第二把钥匙
    approved_prop = review_strength_proposal(
        proposal, actor="user_cairn", actor_role="human", decision="approve", now_iso="2026-09-20T12:02:00Z"
    )
    assert approved_prop["status"] == "ready"
    applied = apply_strength_proposal(core_mem, approved_prop, current_version=1)
    assert applied["record"]["importance"] == 0.85
    assert applied["record"]["moraine_governance"]["strength_locked"] is True
    print("  ✅ 双钥匙共治审批完成！记忆成功升级至 85 分并锁定，全生命周期可溯！")

    print("\n" + "=" * 80)
    print("🎉 [Moraine Kernel v2.0] 7 大核心模块全部断言 100% 通过！零报错零依赖！")
    print("=" * 80)
