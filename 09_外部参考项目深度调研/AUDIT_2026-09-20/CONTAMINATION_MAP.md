# CONTAMINATION_MAP.md

追踪两条独立污染源在 `09_外部参考项目深度调研/` 内的扩散路径。每条边代表"该文件的内容依赖/复述/引用了源头污染"。

---

## 污染源 A：EdgeIM 本体错误串成"并发死锁检测"

```
[污染起点未知——不在本仓可追溯范围内，最早在 9e8adfd/4d79eee 落盘时已是错的]
        │
        ├──> docs/USER_MANUAL.md:85-89
        │      title="EdgeIM: Efficient Detection of Concurrency Bugs in Edge Computing"
        │      引入 T_lock / M_wait 符号，全部虚构
        │
        ├──> docs/MULTI_AGENT_PARALLEL_SPECIFICATION.md:102
        │      P01 | `EdgeIM: Edge Concurrency Bug Detection`
        │      │
        │      └──> prototypes/multi_agent_parallel_harness.py:196
        │             title="解析 EdgeIM 边图模型与死锁定义"
        │             （实际运行会打印这句话，但不影响程序逻辑——纯文本污染，非功能性风险）
        │
        ├──> prototypes/minimal_openviking_kernel.py:302-307
        │      "EdgeIM 提出基于交叉边插桩与轻量 Petri 网可达图分析的并发 Bug 检测机制"
        │      │
        │      └──> 运行时会真实打印到 stdout（已实测，见 AUDIT_FINDINGS.md P0-1）
        │             即该污染已经进入"实测通过"的原型输出里，伪装成验证证据的一部分
        │
        ├──> 06_重点拆解__volcengine__OpenViking_源码级深度剖析与工程移植蓝图.md
        │      §多处（L22, L53-59, L121, L170, L173, L259）反复以
        │      "EdgeIM/SBTPN 并发漏洞挖掘"并列描述
        │      │
        │      └──> 该卷宗 §4.2（L247-277）虚拟目录树本身列出了正确的 11 篇真实论文，
        │             与自己前文的错误描述互相矛盾（同一文件内部不一致）
        │
        ├──> docs/MULTI_KERNEL_SYSTEM_ARCHITECTURE.md:144
        │      "科研台"职责定义为"鲁组并发论文检索、Petri 网验证与死锁重现"
        │      │
        │      └──> 这是四核架构文档，若不修正，会持续引导后续开发把
        │             "科研台"的定位锚定在错误的论文本体上
        │
        ├──> docs/NEXT_PHASE_EXECUTION_PLAN.md:45
        │      Week 4 专项 D 写"驱动多 Agent 并发检测并发死锁与数据竞争"
        │      │
        │      └──> 直接影响下阶段 4 周执行计划的任务定义（见 RECOVERY_PLAN.md 项 7）
        │
        ├──> 09_2026-09-19__窗口全景工作决算与交接总结__window_summary_and_handoff.md:66
        │      LINE-03 写"对接并发死锁检测、Petri 网验证（EdgeIM, SBTPN 等 10 篇论文）"
        │      │
        │      └──> 这是交接文档，若下一个窗口/会话读它作为上下文，会继承错误认知
        │
        └──> 04_试点标杆__PrimeIntellect-ai__prime-agent_源码级深度剖析与工程移植蓝图.md:164
               "鲁组的并发漏洞分析体系中...无幻觉的 Petri 网模型抽取与死锁静态验证"
               │
               └──> 影响 Prime-Agent RLM 机制的"目标业务场景"设定（§4.1），
                      即便 Prime-Agent 拆解本身是扎实的（源码引用可验证），
                      它挂靠的应用场景描述是错的

【独立交叉印证】01_进组总计划_OE1_材料交付/README_进组急用.md:28 (J01 行)
  已独立发现同一污染源，裁定 SOURCE FACT，并在 §4 声明"09 目录...本批未修"
  —— 与本审计互相印证，非孤证；同时证明该轨道已知晓但未越权代为清理 09_ 目录
```

**扩散广度**：9 个文件直接受染（不含 J01 独立发现记录）。**未受染**：`receipts/` 全部原始存证文件（README、trees、sources）——这些是原始抓取材料，本身没有对 EdgeIM 做二次转述，污染只发生在"拆解/整合/规划"层，不在"一手证据留存"层。这是好消息：清理时不需要重新抓取任何原始材料，只需修正转述层。

---

## 污染源 B：P05–P10 六篇虚构论文

```
[起点：docs/MULTI_AGENT_PARALLEL_SPECIFICATION.md:106-111]
      P05 DeadlockPredictor / P06 DataRaceGuard / P07 AsyncPetri /
      P08 FormalEdge / P09 LockTree / P10 HybridRace
        │
        └──> 未发现下游扩散。
               全仓 grep（含 03_全量28仓专项细看计划、NEXT_PHASE_EXECUTION_PLAN、
               MULTI_KERNEL_SYSTEM_ARCHITECTURE、09_window_summary、
               06_OpenViking 卷宗、reports/ 全部 6 份分组报告）均未命中这 6 个名称。
```

**扩散广度**：**仅 1 个文件**，尚未扩散。这是本次审计里最好处理的一项——污染范围极小，且未被其他文档引用或依赖，可以直接删除对应表格行，不需要连锁修复。

**为什么值得单独列为 P0**：不是因为它扩散广，而是因为它的**伪装精度**——6 个假论文名配了假的英文副标题、假的独立写作用域路径、假的 Worker 分配，形式上与 P01-P04（真实论文）完全同构，极易在未来被当作"这个仓库确实有 10 篇论文"的既定事实继承下去。现在拦住成本最低。

---

## 污染源 C：Multi-Agent Harness"实战验证"的证明力被夸大

```
[起点：prototypes/multi_agent_parallel_harness.py 的道具字符串
       (produce_artifact / validation_output 硬编码)]
        │
        ├──> docs/MULTI_AGENT_PARALLEL_SPECIFICATION.md §五
        │      "实测输出证据链"直接贴运行输出，包装成"验证"章节
        │
        ├──> docs/USER_MANUAL.md §四
        │      演示 API 用法时暗示这是可信赖的生产级门禁行为
        │
        └──> docs/MULTI_KERNEL_SYSTEM_ARCHITECTURE.md §二.4
               "控制平面与安全内核"职责描述里，Outcome Floor 被描述为
               "强制要求"级别的门禁，继承了 harness 的证明力夸大
```

**扩散广度**：3 个文档级消费者。核心问题不是"这段代码是假的"（CAS/退避逻辑是真的），而是"文档对这段代码的证明力描述超过了代码实际提供的保证"——这是叙事层夸大，不是代码层造假，修复只需要降级措辞，不需要重写代码。

---

## 未受污染 / 独立验证通过的资产（供对照，避免过度矫正）

- `receipts/sources/headroom/*` + `10_重点拆解__headroomlabs-ai__headroom...md`（净化版）：VERIFIED，三大机制源码锚点精确匹配。
- `receipts/sources/prime-agent/repl.py` + `04_试点标杆__PrimeIntellect-ai__prime-agent...md` 的 file:line 引用（除 §4.1 场景描述受污染源 A 牵连外）：VERIFIED。
- `receipts/repos/loopx/`（4555 文件完整克隆） + `08_重点拆解__huangruiteng__loopx...md` 的全部 8 处 file:line 引用：VERIFIED，逐条核对内容精确匹配，包括对 LoopX 自己代码"legacy 模式脑裂是设计如此"的准确复述。
- `MASTER_EVALUATION_MATRIX.md` 的 28 仓元数据（stars/license/五选一处置）：内部结构自洽，未发现与 `BATCH_METADATA_RECEIPT.json` 矛盾之处（本轮未逐条重新调用 GitHub API 复核，标 NOT_SEARCHED 而非 VERIFIED）。

不建议因为发现了 A/B/C 三条污染，就对整个 `09_外部参考项目深度调研/` 判"全部不可信"——LoopX 与 Prime-Agent 两份拆解卷宗的引用精度实际上相当高，值得保留并作为"正确示范"用于后续 SOP。
