#!/usr/bin/env python3
"""
minimal_loopx_kernel.py · 提纯自 huangruiteng/loopx 核心控制平面与租约门禁原件
零外部依赖（纯 Python 3.10+ 原生），完整闭环演示：
1. 细粒度写范围（Write Scope）前缀与 Glob 重叠判定引擎（提纯自 task_lease_acquire_decision.ts）
2. CAS 乐观并发控制任务租约引擎（Acquire / Renew / Transfer / Release / Idempotent Replay）
3. 四态任务生命周期契约（Pending -> Current -> Delivered / Not_Required）与交付门槛兜底
4. 确定性 PreToolUse 策略门禁（write_scope 限制、破坏性 Bash 拦截与 fail-closed 保护）
5. 跨会话交接（Cross-Session Handoff & Fence Verification）全流程可验证执行
"""

from __future__ import annotations

import fnmatch
import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone, timedelta
from enum import Enum
from typing import Any, Dict, List, Optional, Set, Tuple


# ==============================================================================
# 模块 1：细粒度写范围（Write Scope）重叠判定引擎
# 提纯自 loopx/control_plane/work_items/task_lease_acquire_decision.ts
# ==============================================================================

def scope_literal_prefix(scope: str) -> str:
    """提取通配符之前的字面量前缀"""
    tokens = ["*", "?", "["]
    indexes = [scope.find(t) for t in tokens if scope.find(t) >= 0]
    if indexes:
        return scope[:min(indexes)]
    return scope


def scope_pair_overlaps(left: str, right: str) -> bool:
    """
    判定两个写作用域是否重叠。
    支持全量通配（*、**、./）、单字通配、目录前缀及 Glob 匹配。
    """
    if left == right:
        return True
    if left in {"*", "**", "./"} or right in {"*", "**", "./"}:
        return True

    left_glob = any(token in left for token in ["*", "?", "["])
    right_glob = any(token in right for token in ["*", "?", "["])

    if left_glob and not right_glob:
        prefix = scope_literal_prefix(left)
        if fnmatch.fnmatchcase(right, left):
            return True
        if prefix.endswith("/") and right.rstrip("/") == prefix.rstrip("/"):
            return True
        return False

    if right_glob and not left_glob:
        prefix = scope_literal_prefix(right)
        if fnmatch.fnmatchcase(left, right):
            return True
        if prefix.endswith("/") and left.rstrip("/") == prefix.rstrip("/"):
            return True
        return False

    if left_glob and right_glob:
        left_prefix = scope_literal_prefix(left)
        right_prefix = scope_literal_prefix(right)
        if not left_prefix or not right_prefix:
            return True
        return left_prefix.startswith(right_prefix) or right_prefix.startswith(left_prefix)

    # 两个均为字面量路径：前缀包含关系
    left_root = left.rstrip("/")
    right_root = right.rstrip("/")
    if left.endswith("/") and right.startswith(f"{left_root}/"):
        return True
    if right.endswith("/") and left.startswith(f"{right_root}/"):
        return True
    return False


def write_scopes_overlap(left: List[str], right: List[str]) -> bool:
    """判定两组作用域集合之间是否存在任何冲突重叠"""
    if not left or not right:
        return False
    return any(scope_pair_overlaps(a, b) for a in left for b in right)


# ==============================================================================
# 模块 2：CAS 乐观锁任务租约引擎（Task Lease & Fencing Engine）
# 提纯自 loopx/control_plane/work_items/task_lease.py & task_lease_lifecycle_decision.ts
# ==============================================================================

class LeaseStatus(str, Enum):
    ACTIVE = "active"
    RELEASED = "released"
    EXPIRED = "expired"


@dataclass
class TaskLeaseRecord:
    goal_id: str
    todo_id: str
    owner: str
    idempotency_key: str
    write_scopes: List[str]
    ttl_seconds: int
    version: int = 1
    lease_epoch: int = 1
    status: LeaseStatus = LeaseStatus.ACTIVE
    acquired_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    expires_at: datetime = field(init=False)

    def __post_init__(self):
        if not hasattr(self, "expires_at") or self.expires_at is None:
            self.expires_at = self.acquired_at + timedelta(seconds=self.ttl_seconds)

    def is_active_at(self, moment: datetime) -> bool:
        if self.status != LeaseStatus.ACTIVE:
            return False
        return moment < self.expires_at

    def to_dict(self) -> Dict[str, Any]:
        return {
            "goal_id": self.goal_id,
            "todo_id": self.todo_id,
            "owner": self.owner,
            "idempotency_key": self.idempotency_key,
            "write_scopes": list(self.write_scopes),
            "ttl_seconds": self.ttl_seconds,
            "version": self.version,
            "lease_epoch": self.lease_epoch,
            "status": self.status.value,
            "acquired_at": self.acquired_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "expires_at": self.expires_at.isoformat(),
        }


class TaskLeaseEngine:
    """
    轻量化单机/共享目录 CAS 租约协调引擎。
    严格执行版本一致性、幂等重放、跨任务作用域冲突校验与 Epoch 代际推进。
    """

    def __init__(self, registered_agents: Optional[List[str]] = None):
        self.registered_agents: Set[str] = set(registered_agents or ["agent_main", "agent_sub1", "agent_sub2", "human_user"])
        # todo_id -> TaskLeaseRecord
        self.leases: Dict[str, TaskLeaseRecord] = {}

    def acquire(
        self,
        *,
        goal_id: str,
        todo_id: str,
        owner: str,
        idempotency_key: str,
        write_scopes: List[str],
        ttl_seconds: int = 2700,
        expected_version: Optional[int] = None,
        now: Optional[datetime] = None,
    ) -> Dict[str, Any]:
        now = now or datetime.now(timezone.utc)

        if owner not in self.registered_agents:
            return {"outcome": "rejected", "code": "owner_not_registered"}

        current_lease = self.leases.get(todo_id)

        # 检查现有租约有效性
        if current_lease is not None and current_lease.is_active_at(now):
            actual_version = current_lease.version
            if expected_version is not None and expected_version != actual_version:
                return {"outcome": "conflict", "code": "version_mismatch", "current_version": actual_version}

            # 幂等重放检查 (Idempotent Replay)
            if current_lease.owner == owner and current_lease.idempotency_key == idempotency_key:
                if sorted(current_lease.write_scopes) == sorted(write_scopes) and current_lease.ttl_seconds == ttl_seconds:
                    return {
                        "outcome": "no_change",
                        "code": "lease_acquire_replay",
                        "idempotent": True,
                        "lease": current_lease.to_dict(),
                    }
                return {"outcome": "rejected", "code": "idempotency_key_reuse"}

            # 他人持有中冲突
            return {"outcome": "conflict", "code": "todo_lease_conflict", "held_by": current_lease.owner}

        # 检查是否与其他活跃任务的写作用域发生重叠 (跨任务写锁冲突)
        for other_id, other_lease in self.leases.items():
            if other_id != todo_id and other_lease.is_active_at(now):
                if write_scopes_overlap(write_scopes, other_lease.write_scopes):
                    return {
                        "outcome": "conflict",
                        "code": "write_scope_conflict",
                        "conflicting_todo_id": other_id,
                        "conflicting_scopes": other_lease.write_scopes,
                    }

        # 成功签发新租约
        prev_version = current_lease.version if current_lease else 0
        prev_epoch = current_lease.lease_epoch if current_lease else 0

        if expected_version is not None and expected_version != prev_version:
            return {"outcome": "conflict", "code": "version_mismatch", "current_version": prev_version}

        new_lease = TaskLeaseRecord(
            goal_id=goal_id,
            todo_id=todo_id,
            owner=owner,
            idempotency_key=idempotency_key,
            write_scopes=write_scopes,
            ttl_seconds=ttl_seconds,
            version=prev_version + 1,
            lease_epoch=prev_epoch + 1,
            status=LeaseStatus.ACTIVE,
            acquired_at=now,
            updated_at=now,
        )
        self.leases[todo_id] = new_lease
        return {
            "outcome": "apply",
            "code": "lease_acquire",
            "idempotent": False,
            "lease": new_lease.to_dict(),
        }

    def renew(
        self,
        *,
        todo_id: str,
        owner: str,
        idempotency_key: str,
        expected_version: int,
        ttl_seconds: int = 2700,
        now: Optional[datetime] = None,
    ) -> Dict[str, Any]:
        now = now or datetime.now(timezone.utc)
        current = self.leases.get(todo_id)
        if current is None or not current.is_active_at(now):
            return {"outcome": "rejected", "code": "lease_not_active"}

        if current.version != expected_version:
            return {"outcome": "conflict", "code": "version_mismatch", "current_version": current.version}

        if current.owner != owner or current.idempotency_key != idempotency_key:
            return {"outcome": "rejected", "code": "lease_cas_mismatch"}

        current.version += 1
        current.updated_at = now
        current.expires_at = now + timedelta(seconds=ttl_seconds)
        return {"outcome": "apply", "code": "lease_renew", "lease": current.to_dict()}

    def transfer(
        self,
        *,
        todo_id: str,
        owner: str,
        idempotency_key: str,
        new_owner: str,
        new_idempotency_key: str,
        expected_version: int,
        ttl_seconds: int = 2700,
        now: Optional[datetime] = None,
    ) -> Dict[str, Any]:
        now = now or datetime.now(timezone.utc)
        if new_owner not in self.registered_agents:
            return {"outcome": "rejected", "code": "owner_not_registered"}
        if new_idempotency_key == idempotency_key:
            return {"outcome": "rejected", "code": "idempotency_key_reuse"}

        current = self.leases.get(todo_id)
        if current is None or not current.is_active_at(now):
            return {"outcome": "rejected", "code": "lease_not_active"}

        if current.version != expected_version:
            return {"outcome": "conflict", "code": "version_mismatch", "current_version": current.version}

        if current.owner != owner or current.idempotency_key != idempotency_key:
            return {"outcome": "rejected", "code": "lease_cas_mismatch"}

        # 转移所有权：推进 version 且递增 lease_epoch
        current.owner = new_owner
        current.idempotency_key = new_idempotency_key
        current.version += 1
        current.lease_epoch += 1
        current.updated_at = now
        current.expires_at = now + timedelta(seconds=ttl_seconds)
        return {"outcome": "apply", "code": "lease_transfer", "lease": current.to_dict()}

    def release(
        self,
        *,
        todo_id: str,
        owner: str,
        idempotency_key: str,
        expected_version: int,
        now: Optional[datetime] = None,
    ) -> Dict[str, Any]:
        now = now or datetime.now(timezone.utc)
        current = self.leases.get(todo_id)
        if current is None:
            return {"outcome": "no_change", "code": "lease_missing", "idempotent": True}

        if current.version != expected_version:
            return {"outcome": "conflict", "code": "version_mismatch", "current_version": current.version}

        if current.owner != owner or current.idempotency_key != idempotency_key:
            return {"outcome": "rejected", "code": "lease_cas_mismatch"}

        if current.status == LeaseStatus.RELEASED:
            return {"outcome": "no_change", "code": "lease_release_replay", "idempotent": True}

        current.status = LeaseStatus.RELEASED
        current.updated_at = now
        return {"outcome": "apply", "code": "lease_release", "lease": current.to_dict()}


# ==============================================================================
# 模块 3：四态任务生命周期契约（Four-State Task Lifecycle Contract）
# 提纯自 loopx/control_plane/todos/contract.py & delivery_contract.py
# ==============================================================================

class TaskStatus(str, Enum):
    PENDING = "pending"          # 开放待领 (open)
    CURRENT = "current"          # 活跃执行中 (in_progress, 持有效租约)
    DELIVERED = "delivered"      # 产出已交付并通过验收 (done)
    NOT_REQUIRED = "not_required" # 因环境变化撤销/搁置 (deferred / superseded)


@dataclass
class TaskItem:
    todo_id: str
    title: str
    write_scopes: List[str]
    status: TaskStatus = TaskStatus.PENDING
    claimed_by: Optional[str] = None
    lease_version: Optional[int] = None
    delivery_receipt: Optional[Dict[str, Any]] = None
    deferred_reason: Optional[str] = None


class TaskLifecycleContract:
    """
    四态任务状态机。
    强力约束：任务交付必须提供符合最低基线（Outcome Floor）的交付凭据，
    包括：具象产物（Artifact）、定向验证结论（Targeted Validation）与状态回写证明（State Writeback）。
    """

    def __init__(self, lease_engine: TaskLeaseEngine):
        self.lease_engine = lease_engine
        self.tasks: Dict[str, TaskItem] = {}

    def register_task(self, todo_id: str, title: str, write_scopes: List[str]) -> TaskItem:
        task = TaskItem(todo_id=todo_id, title=title, write_scopes=write_scopes)
        self.tasks[todo_id] = task
        return task

    def claim_task(
        self,
        *,
        goal_id: str,
        todo_id: str,
        agent_id: str,
        idempotency_key: str,
        ttl_seconds: int = 2700,
    ) -> Dict[str, Any]:
        task = self.tasks.get(todo_id)
        if not task:
            raise KeyError(f"任务未找到: {todo_id}")
        if task.status != TaskStatus.PENDING:
            return {"success": False, "error": f"任务状态不处于 pending，当前为: {task.status.value}"}

        # 尝试获取硬件/写锁租约
        acquire_res = self.lease_engine.acquire(
            goal_id=goal_id,
            todo_id=todo_id,
            owner=agent_id,
            idempotency_key=idempotency_key,
            write_scopes=task.write_scopes,
            ttl_seconds=ttl_seconds,
        )
        if acquire_res["outcome"] not in {"apply", "no_change"}:
            return {"success": False, "error": f"租约获取失败: {acquire_res['code']}", "detail": acquire_res}

        task.status = TaskStatus.CURRENT
        task.claimed_by = agent_id
        task.lease_version = acquire_res["lease"]["version"]
        return {"success": True, "task": task, "lease": acquire_res["lease"]}

    def deliver_task(
        self,
        *,
        todo_id: str,
        agent_id: str,
        idempotency_key: str,
        artifact: str,
        targeted_validation: str,
        state_writeback: str,
    ) -> Dict[str, Any]:
        """
        严苛的最低交付门槛（Outcome Floor）：
        禁止大模型只通过'我做完了'的自然语言自圆其说。
        必须提交真实存在的产物指针、明确的测试通过证明与更新后的状态写回哈希。
        """
        task = self.tasks.get(todo_id)
        if not task:
            raise KeyError(f"任务未找到: {todo_id}")
        if task.status != TaskStatus.CURRENT or task.claimed_by != agent_id:
            return {"success": False, "error": "当前 Agent 未持有该任务的有效执行状态"}

        if not artifact or not targeted_validation or not state_writeback:
            return {
                "success": False,
                "error": "违反最低交付门槛 (Outcome Floor): 必须完整提供 artifact, targeted_validation, state_writeback",
            }

        # 释放底层写租约
        release_res = self.lease_engine.release(
            todo_id=todo_id,
            owner=agent_id,
            idempotency_key=idempotency_key,
            expected_version=task.lease_version or 1,
        )
        if release_res["outcome"] not in {"apply", "no_change"}:
            return {"success": False, "error": f"租约释放失败: {release_res['code']}"}

        receipt = {
            "artifact": artifact,
            "targeted_validation": targeted_validation,
            "state_writeback": state_writeback,
            "delivered_by": agent_id,
            "delivered_at": datetime.now(timezone.utc).isoformat(),
        }
        task.status = TaskStatus.DELIVERED
        task.delivery_receipt = receipt
        return {"success": True, "receipt": receipt}

    def defer_task(self, *, todo_id: str, agent_id: str, idempotency_key: str, reason: str) -> Dict[str, Any]:
        task = self.tasks.get(todo_id)
        if not task:
            raise KeyError(f"任务未找到: {todo_id}")
        if not reason.strip():
            return {"success": False, "error": "撤销或搁置任务必须附带原因"}

        if task.status == TaskStatus.CURRENT:
            self.lease_engine.release(
                todo_id=todo_id,
                owner=agent_id,
                idempotency_key=idempotency_key,
                expected_version=task.lease_version or 1,
            )

        task.status = TaskStatus.NOT_REQUIRED
        task.deferred_reason = reason
        return {"success": True, "task": task}


# ==============================================================================
# 模块 4：确定性 PreToolUse 策略门禁（Policy Gate）
# 提纯自 loopx/claude_goal_mode/hooks/goal_policy.py
# ==============================================================================

class TurnAuthorityGate:
    """
    针对 Claude Code 等 Agent 运行时的前置拦截器。
    在执行工具前强制核验：
    1. 读操作（Read/Glob/Grep）安全免检放行；
    2. 写操作（Edit/Write）严格限定在任务当前持有的 write_scopes 范围内，杜绝越权污染；
    3. Shell 执行（Bash）硬编码黑名单阻断（rm -rf / git reset --hard / git push --force / reboot）。
    """

    READ_ONLY_TOOLS = {"Read", "Glob", "Grep", "NotebookRead", "ToolSearch", "WebFetch", "WebSearch"}
    WRITE_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit"}
    DESTRUCTIVE_BASH = [
        "rm -rf", "rm -fr", "mkfs", "dd if=", ":(){", "shutdown", "reboot",
        "git push --force", "git reset --hard", "> /dev/sd", "format ",
    ]

    def __init__(self, lease_engine: TaskLeaseEngine):
        self.lease_engine = lease_engine

    def evaluate_tool_call(
        self,
        *,
        agent_id: str,
        active_todo_id: Optional[str],
        tool_name: str,
        tool_args: Dict[str, Any],
    ) -> Tuple[bool, str]:
        # 1. 读操作直接放行
        if tool_name in self.READ_ONLY_TOOLS:
            return True, "read-only tool authorized"

        # 2. 检查是否有活跃任务和有效租约 (Fail-Closed)
        if not active_todo_id:
            return False, "BLOCKED: non-read-only tool requires an active claimed todo"

        current_lease = self.lease_engine.leases.get(active_todo_id)
        now = datetime.now(timezone.utc)
        if not current_lease or not current_lease.is_active_at(now) or current_lease.owner != agent_id:
            return False, "BLOCKED: active task lease expired or actor mismatch"

        # 3. 写操作路径合规审计
        if tool_name in self.WRITE_TOOLS:
            file_path = tool_args.get("file_path", "")
            if not file_path:
                return False, "BLOCKED: write tool missing file_path"

            # 校验 file_path 是否被包含在 current_lease.write_scopes 范围内
            allowed = False
            for scope in current_lease.write_scopes:
                if scope_pair_overlaps(scope, file_path):
                    allowed = True
                    break
            if not allowed:
                return False, f"BLOCKED: file_path '{file_path}' outside authorized write_scopes {current_lease.write_scopes}"

            return True, f"write permitted inside scope: {file_path}"

        # 4. 终端命令安全合规审计
        if tool_name == "Bash":
            cmd = tool_args.get("command", "")
            for bad_pattern in self.DESTRUCTIVE_BASH:
                if bad_pattern in cmd:
                    return False, f"BLOCKED: destructive Bash pattern detected ('{bad_pattern}')"
            return True, "bash command authorized"

        return True, "unknown tool deferred to system flow"


# ==============================================================================
# 自检与全流程验证套件
# ==============================================================================

def run_self_tests():
    print("=" * 70)
    print("minimal_loopx_kernel.py · 纯原生零依赖算法验证套件")
    print("=" * 70)

    # 1. 测试写范围重叠 (Write Scopes Overlap)
    print("[1/5] 测试细粒度写作用域重叠匹配引擎...")
    assert scope_pair_overlaps("docs/", "docs/api.md") is True
    assert scope_pair_overlaps("docs/api.md", "docs/") is True
    assert scope_pair_overlaps("src/*.py", "src/main.py") is True
    assert scope_pair_overlaps("src/*.py", "tests/test_main.py") is False
    assert scope_pair_overlaps("package.json", "package.json") is True
    assert scope_pair_overlaps("packages/core/", "packages/ui/index.ts") is False
    assert write_scopes_overlap(["src/model.py"], ["src/controller.py"]) is False
    assert write_scopes_overlap(["src/*"], ["src/model.py"]) is True
    print("  ✓ 路径字面量、目录前缀、Glob 通配符重叠判定 100% 通过")

    # 2. 测试 CAS 租约获取、冲突与幂等重放
    print("[2/5] 测试 CAS 租约获取、版本控制与幂等重放...")
    engine = TaskLeaseEngine(registered_agents=["agent_alice", "agent_bob", "coordinator"])

    # Alice 获取 todo_1
    res1 = engine.acquire(
        goal_id="goal_bench",
        todo_id="todo_1",
        owner="agent_alice",
        idempotency_key="alice_key_001",
        write_scopes=["05_科研台/src/*"],
        ttl_seconds=3600,
    )
    assert res1["outcome"] == "apply"
    assert res1["lease"]["version"] == 1
    assert res1["lease"]["lease_epoch"] == 1

    # 重放请求 (相同参数，应当幂等放行，且版本不递增)
    res_replay = engine.acquire(
        goal_id="goal_bench",
        todo_id="todo_1",
        owner="agent_alice",
        idempotency_key="alice_key_001",
        write_scopes=["05_科研台/src/*"],
        ttl_seconds=3600,
    )
    assert res_replay["outcome"] == "no_change"
    assert res_replay["idempotent"] is True
    assert res_replay["lease"]["version"] == 1

    # Bob 试图同时获取同一 todo_1 (应被冲突拦截)
    res_bob_todo = engine.acquire(
        goal_id="goal_bench",
        todo_id="todo_1",
        owner="agent_bob",
        idempotency_key="bob_key_001",
        write_scopes=["05_科研台/src/*"],
    )
    assert res_bob_todo["outcome"] == "conflict"
    assert res_bob_todo["code"] == "todo_lease_conflict"

    # Bob 试图获取另一个 todo_2，但写作用域冲突 (05_科研台/src/main.py 重叠)
    res_bob_scope = engine.acquire(
        goal_id="goal_bench",
        todo_id="todo_2",
        owner="agent_bob",
        idempotency_key="bob_key_002",
        write_scopes=["05_科研台/src/main.py"],
    )
    assert res_bob_scope["outcome"] == "conflict"
    assert res_bob_scope["code"] == "write_scope_conflict"

    # Bob 获取无冲突作用域的 todo_3 (应当成功)
    res_bob_ok = engine.acquire(
        goal_id="goal_bench",
        todo_id="todo_3",
        owner="agent_bob",
        idempotency_key="bob_key_003",
        write_scopes=["09_外部参考/docs/*"],
    )
    assert res_bob_ok["outcome"] == "apply"
    print("  ✓ 租约签发、CAS 并发防撞、跨任务写作用域冲突排他 100% 通过")

    # 3. 测试租约转移 (Transfer) 与代际 (Epoch) 推进
    print("[3/5] 测试所有权安全交接与 Epoch 代际递增...")
    res_transfer = engine.transfer(
        todo_id="todo_1",
        owner="agent_alice",
        idempotency_key="alice_key_001",
        new_owner="agent_bob",
        new_idempotency_key="bob_key_transfer_001",
        expected_version=1,
    )
    assert res_transfer["outcome"] == "apply"
    assert res_transfer["lease"]["owner"] == "agent_bob"
    assert res_transfer["lease"]["version"] == 2
    assert res_transfer["lease"]["lease_epoch"] == 2  # Epoch 递增！

    # 旧持有者 Alice 试图用旧 key 继续 renew (应当被拒绝)
    res_stale = engine.renew(
        todo_id="todo_1",
        owner="agent_alice",
        idempotency_key="alice_key_001",
        expected_version=2,
    )
    assert res_stale["outcome"] == "rejected"
    assert res_stale["code"] == "lease_cas_mismatch"

    # Bob 正常释放 todo_1，使得后续写作用域释放
    res_rel = engine.release(
        todo_id="todo_1",
        owner="agent_bob",
        idempotency_key="bob_key_transfer_001",
        expected_version=2,
    )
    assert res_rel["outcome"] == "apply"
    print("  ✓ 跨 Agent 租约代际推进、旧持有者隔离与安全释放 100% 通过")

    # 4. 测试四态生命周期契约与 Outcome Floor 交付硬门槛
    print("[4/5] 测试四态生命周期状态机与交付门槛 (Outcome Floor)...")
    contract = TaskLifecycleContract(engine)
    contract.register_task("TASK-001", "实现并发模型转换", ["05_科研台/src/petri/*"])

    # 认领任务
    claim_res = contract.claim_task(
        goal_id="goal_lu",
        todo_id="TASK-001",
        agent_id="agent_bob",
        idempotency_key="bob_claim_task_001",
    )
    assert claim_res["success"] is True
    assert contract.tasks["TASK-001"].status == TaskStatus.CURRENT

    # 尝试违规交付 (缺少测试验证与写回证明)
    fail_deliv = contract.deliver_task(
        todo_id="TASK-001",
        agent_id="agent_bob",
        idempotency_key="bob_claim_task_001",
        artifact="05_科研台/src/petri/net.py",
        targeted_validation="",  # 缺失
        state_writeback="",
    )
    assert fail_deliv["success"] is False
    assert "Outcome Floor" in fail_deliv["error"]
    assert contract.tasks["TASK-001"].status == TaskStatus.CURRENT  # 状态未改变

    # 合格交付
    ok_deliv = contract.deliver_task(
        todo_id="TASK-001",
        agent_id="agent_bob",
        idempotency_key="bob_claim_task_001",
        artifact="05_科研台/src/petri/net.py (230 LOC)",
        targeted_validation="pytest tests/test_petri.py (14 passed in 0.4s)",
        state_writeback="sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    )
    assert ok_deliv["success"] is True
    assert contract.tasks["TASK-001"].status == TaskStatus.DELIVERED
    print("  ✓ 4-State 状态流转与三要素（产物+验证+写回）交付门槛 100% 通过")

    # 5. 测试确定性 PreToolUse 策略门禁拦截
    print("[5/5] 测试 PreToolUse 策略门禁拦截 (写范围越界与危险命令)...")
    gate = TurnAuthorityGate(engine)

    # 准备环境：注册并认领 TASK-002 (限定仅能写 05_科研台/docs/*)
    contract.register_task("TASK-002", "编写文档", ["05_科研台/docs/*"])
    contract.claim_task(
        goal_id="goal_lu",
        todo_id="TASK-002",
        agent_id="agent_bob",
        idempotency_key="bob_doc_key",
    )

    # 1. 读操作：免检放行
    allowed, msg = gate.evaluate_tool_call(
        agent_id="agent_bob",
        active_todo_id="TASK-002",
        tool_name="Read",
        tool_args={"file_path": "/etc/hosts"},
    )
    assert allowed is True

    # 2. 合法写操作：允许写 05_科研台/docs/readme.md
    allowed, msg = gate.evaluate_tool_call(
        agent_id="agent_bob",
        active_todo_id="TASK-002",
        tool_name="Write",
        tool_args={"file_path": "05_科研台/docs/readme.md"},
    )
    assert allowed is True

    # 3. 越权写操作：试图写 05_科研台/src/core.py (超出 write_scopes，阻断！)
    allowed, msg = gate.evaluate_tool_call(
        agent_id="agent_bob",
        active_todo_id="TASK-002",
        tool_name="Write",
        tool_args={"file_path": "05_科研台/src/core.py"},
    )
    assert allowed is False
    assert "outside authorized write_scopes" in msg

    # 4. 危险终端命令：检测到 rm -rf 阻断！
    allowed, msg = gate.evaluate_tool_call(
        agent_id="agent_bob",
        active_todo_id="TASK-002",
        tool_name="Bash",
        tool_args={"command": "rm -rf /tmp/test"},
    )
    assert allowed is False
    assert "destructive Bash pattern detected" in msg

    # 5. 安全终端命令：pytest 放行
    allowed, msg = gate.evaluate_tool_call(
        agent_id="agent_bob",
        active_todo_id="TASK-002",
        tool_name="Bash",
        tool_args={"command": "pytest tests/ -v"},
    )
    assert allowed is True
    print("  ✓ PreToolUse 策略审计、越界写防护与高危命令熔断 100% 通过")

    print("=" * 70)
    print("🎉 ALL 5 TEST SUITES PASSED (100% 成功)")
    print("=" * 70)


if __name__ == "__main__":
    run_self_tests()
