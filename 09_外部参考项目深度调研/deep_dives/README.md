# L3 源码级硬核深度审计专区 (Deep Dives)

本专区是针对 28 仓中具备最高战略价值与技术突破性的 **核心工程项目** 开展的 **“手术刀式源码静态审查与底层代码解剖”**。

拒绝二手技术博客式的概括宣传，全部内容均基于抓取到本地的真实源码（`receipts/sources/`）逐行核验而成，涵盖通信协议、底层数据结构、状态机状态转移、防踩坑边界与可直接复用的硬核代码。

---

## 核心解剖专题清单

1. **[01 · Prime Agent 递归智能体内核与持续支架](./01_prime_agent__rlm_kernel_and_continual_harness__source_audit.md)**
   - **核验源码**：`repl.py` (49.2KB), `harness.py` (38.8KB), `refine.py` (1.8KB)
   - **核心突破**：CPython 常驻 REPL 进程 + stdio 双向 JSON-RPC 协议；RLM `prompt-as-variable` 变量化子代理调用；`_ALWAYS_SKIP` 内存快照隔离；回合尾部（Turn-end）原子化 Prompt 微调；CJK 东亚文字二元分词（Bigrams）。
2. **[02 · OpenViking-Plugins 基于 Claude Code 原生 Hooks 的记忆闭环](./02_openviking_plugins__claude_code_native_hooks__source_audit.md)**
   - **核验源码**：`hooks.json`, `auto-recall.mjs` (12.8KB), `auto-capture.mjs` (11.3KB), `memory-server.ts` (26.4KB)
   - **核心突破**：利用 `UserPromptSubmit` Hook 静默注入 `<relevant-memories>`；四维加权（向量相似度 + 树层级 + 时间意图 + 词法重叠）防记忆污染；利用 `Stop` Hook 配合 `capturedTurnCount` 游标实现增量对话记忆提纯。
3. **[03 · Headroom 本地上下文压缩与缓存边界守卫机制](./03_headroom__context_compression_and_cache_control__source_audit.md)**
   - **核验源码**：`crates/headroom-core/src/lib.rs`, `cache_control.rs` (15.4KB), `compression_benchmark.py` (33KB)
   - **核心突破**：Rust 零正则 AST 解析；严苛的 `compute_frozen_count` 缓存守卫算法，绝对冻结带有 `cache_control` 的前缀消息，确保 Anthropic Prompt Cache 命中率 100%；仅对活跃区（Live Zone）工具输出进行局部小模型无损压缩。
4. **[04 · LoopX 长程智能体有状态控制面与租约门禁机制](./04_loopx__long_horizon_control_plane_and_gates__source_audit.md)**
   - **核验源码**：`rfc-control-plane.md` (124.6KB), `lark-authority-protocol.md` (4.4KB), `services.rs` (43.6KB)
   - **核心突破**：解耦 Harness（执行有界动作）与 Control Plane（维持长周期状态）；任务生命周期四态转移契约（`pending` -> `current` -> `delivered` -> `not_required`）；CAS 乐观锁与租约隔离（Lease Fence）消灭多 Agent 写冲突；消息可见性与执行权限严格隔离。
5. **[05 · i-have-adhd 认知载荷优化与防废话提示词契约](./05_i_have_adhd__anti_rambling_prompt_contract__source_audit.md)**
   - **核验源码**：`skills/i-have-adhd/SKILL.md` (7.2KB)
   - **核心突破**：十条高压行动导向防废话铁律；三类严打违禁句式（开场客套、事后复述、客套结语）；发送前五项强制自检过滤器（Pre-send Check）；Debug Spiral 死循环熔断机制。
