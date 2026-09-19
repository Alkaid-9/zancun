# 多核驱动系统操作使用手册 (User & Operator Manual)

- **适用对象**：研发人员、科研人员及自主 Agent 执行器
- **归档路径**：`09_外部参考项目深度调研/docs/USER_MANUAL.md`
- **运行环境要求**：Python 3.10+（纯标准库，零 pip 安装依赖）

---

## 一、快速上手：三套原型开箱自检

进入项目根目录后，可直接通过 Python 命令行一键运行三套提纯原型进行功能自检：

```bash
cd /mnt/d/Alkaid/Desktop/2026-09_进组计划与产出_按项目与论文归类_截至2026-09-19

# 1. 验证 Moraine 双时态伴侣记忆治理内核 (280 LOC)
python3 09_外部参考项目深度调研/prototypes/minimal_moraine_kernel.py

# 2. 验证 OpenViking 虚拟语义树与论文分级装配内核 (290 LOC)
python3 09_外部参考项目深度调研/prototypes/minimal_openviking_kernel.py

# 3. 验证 LoopX CAS 租约、写范围排他与交付门禁内核 (756 LOC)
python3 09_外部参考项目深度调研/prototypes/minimal_loopx_kernel.py
```

若屏幕输出 `ALL TEST SUITES PASSED` 或 `100% 成功`，证明当前本地 Python 运行时完全达标。

---

## 二、记忆治理内核（Moraine Kernel）API 使用指引

对应模块：`prototypes/minimal_moraine_kernel.py`

### 1. 双时态事实合法性判定
```python
from minimal_moraine_kernel import is_record_valid_at, parse_iso_utc
from datetime import datetime, timezone

# 构造一条带真实世界有效期的事实
fact = {
    "content": "张重熙当前住在北京市海淀区中关村",
    "valid_from": "2026-01-01T00:00:00Z",
    "valid_to": "2026-09-01T00:00:00Z" # 2026年9月已失效迁出
}

# 判定 2026-05-01 时刻事实是否成立
moment_may = datetime(2026, 5, 1, tzinfo=timezone.utc)
assert is_record_valid_at(fact, moment_may) is True

# 判定当前（2026-09-19）事实是否成立
moment_now = datetime(2026, 9, 19, tzinfo=timezone.utc)
assert is_record_valid_at(fact, moment_now) is False  # 已平滑退出活跃视图，不产生幻觉
```

### 2. 保守抽取式去重（杜绝大模型模糊改写）
```python
from minimal_moraine_kernel import consolidate_memories

records = [
    {"id": "m1", "content": "张重熙喜欢喝冰美式咖啡。"},
    {"id": "m2", "content": "张重熙喜欢喝冰美式咖啡。明天要去实验室。"}, # m1 被 m2 完全字面蕴含
]

res = consolidate_memories(records)
print(res["consolidated_content"])
# 输出: 张重熙喜欢喝冰美式咖啡。明天要去实验室。
# m1 自动以 reason: 'subsumed_verbatim' 被安全剔除，保留完整原始句子字面量
```

---

## 三、上下文文件系统内核（OpenViking Kernel）API 使用指引

对应模块：`prototypes/minimal_openviking_kernel.py`

### 1. 挂载鲁组学术论文至虚拟目录树
```python
from minimal_openviking_kernel import VikingFileSystem, HierarchicalContextAssembler

vfs = VikingFileSystem()

# 挂载鲁组并发死锁检测论文 (EdgeIM)
vfs.mount_resource(
    uri="viking://papers/concurrency/edge_im_2020",
    title="EdgeIM: Efficient Detection of Concurrency Bugs in Edge Computing",
    abstract="提出了基于边图模型的并发死锁与数据竞争动态检测机制，运行开销降低 65%...", # L0
    overview="## 核心章节\n1. 边图构建\n2. 锁依赖传递\n3. 符号化验证\n符号表: G=(V,E), T_lock, M_wait", # L1
    detail="定理 1 证明: 设 G 为有向锁依赖图，若存在环路 C 使得所有边满足并发可达性...", # L2
    tags=["concurrency", "deadlock", "edge_computing"],
)
```

### 2. 在严苛 Token 预算下自适应装配上下文
```python
assembler = HierarchicalContextAssembler(vfs)

# 场景 A：单次提问 Token 预算极度紧张 (例如仅留 180 Tokens 给论文背景)
ctx_compact = assembler.assemble_context(
    query="死锁检测的边图构造算法",
    token_budget=180
)
print(ctx_compact)
# 自动按 L0(摘要) + L1(提纲与符号表) 装配，绝不暴力截断定理证明，保证基础语义完整

# 场景 B：高预算深度定理证明 (预算充裕 2000 Tokens)
ctx_full = assembler.assemble_context(
    query="定理 1 证明的环路依赖定理全文",
    token_budget=2000
)
# 相关度 Score >= 0.85 的具体章节将自动展开 L2 全文，实现高保真数学论证
```

---

## 四、控制平面与任务租约内核（LoopX Kernel）API 使用指引

对应模块：`prototypes/minimal_loopx_kernel.py`

### 1. 申请 CAS 任务租约与防并发冲突
```python
from minimal_loopx_kernel import TaskLeaseEngine

engine = TaskLeaseEngine(registered_agents=["agent_main", "agent_sub1", "agent_sub2"])

# Agent 1 申请认领任务，锁定写范围
res = engine.acquire(
    goal_id="goal_concurrency_audit",
    todo_id="TASK-20260919-001",
    owner="agent_main",
    idempotency_key="main_token_001",
    write_scopes=["05_科研台/src/petri/*"], # 锁定 Petri 网源码目录
    ttl_seconds=3600,
)
assert res["outcome"] == "apply"
print("租约签发成功，版本:", res["lease"]["version"])

# Agent 2 试图同时修改相同目录，将被立即拦截
conflict_res = engine.acquire(
    goal_id="goal_concurrency_audit",
    todo_id="TASK-20260919-002",
    owner="agent_sub1",
    idempotency_key="sub1_token_001",
    write_scopes=["05_科研台/src/petri/validator.py"], # 命中 Glob 重叠冲突！
)
assert conflict_res["outcome"] == "conflict"
assert conflict_res["code"] == "write_scope_conflict"
print("并发写冲突拦截成功:", conflict_res["code"])
```

### 2. 四态任务流转与 Outcome Floor 最低交付验收
```python
from minimal_loopx_kernel import TaskLifecycleContract

contract = TaskLifecycleContract(engine)
contract.register_task("TASK-001", "实现 Petri 网死锁判定", ["05_科研台/src/petri/*"])
contract.claim_task(goal_id="goal_1", todo_id="TASK-001", agent_id="agent_main", idempotency_key="key_1")

# 试图“口头”交付任务（无测试报告与写回指纹）
fail_deliv = contract.deliver_task(
    todo_id="TASK-001",
    agent_id="agent_main",
    idempotency_key="key_1",
    artifact="src/net.py",
    targeted_validation="", # 缺失！
    state_writeback="",     # 缺失！
)
assert fail_deliv["success"] is False
print("口头假汇报被拒:", fail_deliv["error"])

# 合规交付（包含产物、单元测试证据与状态写回指纹）
ok_deliv = contract.deliver_task(
    todo_id="TASK-001",
    agent_id="agent_main",
    idempotency_key="key_1",
    artifact="05_科研台/src/petri/net.py (230 LOC)",
    targeted_validation="pytest tests/test_petri.py (14 passed in 0.4s)",
    state_writeback="sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
)
assert ok_deliv["success"] is True
print("交付成功，任务已置为 delivered 状态！")
```

### 3. PreToolUse 策略门禁拦截高危命令
```python
from minimal_loopx_kernel import TurnAuthorityGate

gate = TurnAuthorityGate(engine)

# 校验 Bash 命令
allowed, msg = gate.evaluate_tool_call(
    agent_id="agent_main",
    active_todo_id="TASK-001",
    tool_name="Bash",
    tool_args={"command": "rm -rf /mnt/d/Workspace"} # 注入危险命令！
)
assert allowed is False
print("系统拦截危险操作:", msg)
# 输出: BLOCKED: destructive Bash pattern detected ('rm -rf')
```
