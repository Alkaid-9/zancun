# L3 源码深度剖析 04 · huangruiteng/loopx 长程智能体有状态控制面与租约门禁机制

- **审查对象**：`huangruiteng/loopx`
- **审计深度**：**L3 源码与系统架构级（RFC 协议与 Rust/TS 实现审查）**
- **本地源码凭证**：
  - `receipts/sources/loopx/rfc-control-plane.md`（124.6 KB 控制平面从 Python 到 TS 迁移的完整架构 RFC）
  - `receipts/sources/loopx/lark-authority-protocol.md`（4.4 KB 消息可见性与执行权限隔离规范）
  - `receipts/sources/loopx/services.rs`（43.6 KB Tauri/Rust 桌面原生控制服务调度底座）

---

## 1. 痛点根治：为什么单靠 Prompt 和 TodoList 搞不定长程复杂工程？

市面上多数智能体系统，一旦任务跨越数天、经历多次 Claude 窗口重启或多 Agent 并发，就会产生以下典型崩塌：
1. **幽灵任务（Ghost Tasks）**：多个子代理同时修改一个 Todo 文件，互相覆盖产生竞态条件（Race Conditions）；
2. **权限越权与无感扣费**：群里有人随便聊一句，机器人误以为是命令，未经授权擅自启动耗费大量 Token 的昂贵流程；
3. **证据链丢失（Evidence Loss）**：上一个窗口声称“代码已改完并通过测试”，但新窗口不知道去哪里检验真实证据（Receipts），只能重做一遍或盲目信任。

**LoopX 的核心贡献**：
它将自己定位于 **“长程循环工程（Loop Engineering）的控制平面”**，核心原则是：**“Harness 负责执行有边界的动作，LoopX 负责持久化维持跨窗口状态”**。

```
       人类管理者 (Lark/CLI/Dashboard)
                   │
                   ▼ (Turn Authority 显式授权)
┌──────────────────────────────────────────────────────────────┐
│                    LoopX 控制平面 (Control Plane)            │
│                                                              │
│  - 目标状态机 (Objectives & 4-State Contract)                │
│  - 租约隔离更新 (Lease-Fenced Canonical Updates)              │
│  - 存证回执鉴真 (AuthorityStore & Evidence Receipts)          │
└──────────────────────────────┬───────────────────────────────┘
                               │ CAS 乐观锁派发有界任务
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                 执行外壳 (Harness: Claude Code)              │
│  - 纯粹执行读写、测试、编码动作                              │
│  - 输出结构化 Witness/Receipts 提交回控制平面                │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. 核心架构解剖：四大状态约束与租约锁（Lease Fence）

### 2.1 任务生命周期的四状态契约（The Four-State Contract）
在 `rfc-control-plane.md:35-41` 中，LoopX 废弃了含糊不清的“正在进行/已完成”两态，强制使用严格的四态转移：
- **`pending`（等待就绪）**：前置依赖尚未满足，严禁分配 Agent；
- **`delivered`（已交付待验收）**：Agent 执行完毕，已提供命令退出码与文件修改回执，等待 CAS 验证；
- **`current`（当前活跃租约）**：唯一的有效租约持有者，其他人只读；
- **`not_required`（已被置换/废止）**：因上游目标变化而安全撤回。

### 2.2 租约隔离（Lease-Fenced Updates）防多 Agent 踏踏
看 `rfc-control-plane.md:72-81` 的实现：
```typescript
// 伪代码表示其核心 CAS 校验逻辑
function updateTodoWithLease(todoId, intent, activeLeaseKey, expectedRevision) {
    const currentHead = AuthorityStore.get(todoId);
    if (currentHead.leaseKey !== activeLeaseKey) {
        throw new Error("Lease mismatch: task has been reclaimed or expired");
    }
    if (currentHead.revision !== expectedRevision) {
        throw new Error("CAS conflict: task modified by peer agent");
    }
    return AuthorityStore.commit(todoId, intent);
}
```
**深度见解**：
当我们在工作台中拉起多个子代理（如一个修前端、一个修后端）时，子代理更新任务必须携带 `active execution key` 和 `lease version`。如果某个子代理超时退出，租约被收回，它即便后续返回结果也无法覆盖现有进度，彻底消灭了多 Agent 并发写冲突。

---

## 3. 核心协议解剖：`lark-authority-protocol.md`（消息可见性与执行权限分离）

在 `lark-authority-protocol.md:5-24` 中，定义了一个极其重要的安全准则：
> **“LoopX 将消息可见性（Message Visibility）与执行权限（Turn Authority）分开处理。”**

- **仅保留（Context-Only）**：来自工作群的讨论、报错反馈、日常交流，虽然会被捕获进本地上下文，但它们**严格打上 `context-only` 标签**，Prompt 明确声明这些**不是命令，不是授权，严禁触发任何 Goal/Todo 的修改**！
- **真正授权（Authorized Turn）**：必须包含显式的 @Bot 动作、经过鉴权的审批指令或 typed authority 记录，Agent 才能消耗预算执行写操作。

---

## 4. 对我们“两台与工作台”的落地复用方案

| 偷师模块 | 对应源码/协议 | 拟引入到本项目的哪部分 | 收益与解决的痛点 |
|---|---|---|---|
| **消息可见性与执行权限严格隔离** | `lark-authority-protocol.md` | 工作台用户输入鉴权层 | 杜绝模型把上下文里的历史提问、讨论猜测当作最新强制指令去执行 |
| **四状态契约与租约锁** | `rfc-control-plane.md` | `09_外部参考项目深度调研` 及两台任务账本 | 解决跨窗口交接（Handoff）时任务状态模糊、多轮修改冲突的问题 |
| **证据鉴真门禁（Evidence Receipts）** | `AuthorityStore receipt boundary` | AC 验收与进度更新守卫 | 任何声称完成的任务必须挂载真实执行命令与测试回执，才能打勾关闭 |
