# STATE_RECLASSIFICATION.md

对 `09_外部参考项目深度调研/` 主要资产重新分级。状态集合采用用户指令 §5 的枚举，不使用单一 DONE。

| 资产 | 旧状态（文档自称） | 新状态（本次审计裁定） | 裁定依据 |
|---|---|---|---|
| `10_重点拆解__headroomlabs-ai__headroom_...md` + `minimal_headroom_kernel.py` | "已完成五模块硬核剖析与最小原型实测" | **SOURCE_VERIFIED**（机制部分）+ **TOY_TESTED**（原型部分）+ **UNVERIFIED**（benchmark 具体百分比数字） | 三大机制 file:line 锚点与本地 receipts 精确匹配；原型是零依赖纯函数单测；benchmark 表格数字无执行 receipt |
| `08_重点拆解__huangruiteng__loopx_...md` | "已完成源码级深度剖析" | **SOURCE_VERIFIED** | 全部 8 处 file:line 引用逐条核对，与 `receipts/repos/loopx/` 完整克隆内容精确匹配，含准确复述上游"legacy split-brain by design"的自我承认 |
| `04_试点标杆__PrimeIntellect-ai__prime-agent_...md` | "5大硬核模块落地样本"，终审标杆 | **SOURCE_VERIFIED**（源码引用部分）/ **CONTAMINATED**（§4.1 应用场景描述，因牵连污染源 A） | repl.py:1027-1036 等引用精确匹配；但"鲁组并发漏洞分析体系"场景设定继承了错误的 EdgeIM 本体 |
| `06_重点拆解__volcengine__OpenViking_...md` | "已完成三篇论文分级挂载验证" | **CONTAMINATED**（叙述层） + **RECONSTRUCTION**（§4.2 目录树结构本身是对的） | 反复用错误的 EdgeIM 本体描述，但虚拟目录树列出的 11 篇论文清单是准确的——同一文件内部两种状态并存，需分段精确修复而非整体推翻 |
| `docs/USER_MANUAL.md` | 隐含"可信操作手册" | **CONTAMINATED**（§三.1 EdgeIM 挂载示例） / **TOY_TESTED**（其余 API 示例） | 唯一污染点在 §三.1 的 EdgeIM 示例数据；Moraine/LoopX 章节的 API 示例本身准确对应源码行为 |
| `docs/MULTI_AGENT_PARALLEL_SPECIFICATION.md` | "配套可运行原型（实测 100% PASS）" | **FABRICATED**（P05-P10 表格） + **TOY_TESTED**（四级隔离模型的机制描述） + **AGENT_GENERATED, unverified claim strength**（"10 篇论文数十秒完成"推论） | P05-P10 六篇论文查无实据；CAS/write-scope/backoff 机制描述与源码一致；但"数十秒完成 10 篇论文"缺乏真实 Agent 执行支撑 |
| `prototypes/multi_agent_parallel_harness.py` | "多 Agent 并发协同与写隔离实战验证支架（已实测100%通过）" | **TOY_TESTED**（CAS 租约/退避逻辑） + **NOT integration_tested**（产物/测试声称） | 真实执行确认线程调度与重试逻辑工作；但 `produce_artifact`/`validation_output` 是硬编码字符串，磁盘核验确认对应文件不存在 |
| `prototypes/minimal_loopx_kernel.py` | "已实测100%通过" | **TOY_TESTED** | 自测通过，且此次独立复核确认 `deliver_task` 门禁逻辑与文档描述的"强制拒签"存在能力差距（只做非空校验），但作为 toy 组件本身表现符合其代码实际承诺 |
| `prototypes/minimal_openviking_kernel.py` | "已实测100%通过" | **TOY_TESTED**（机制） + **CONTAMINATED**（demo 数据） | AsyncSemaphore/分级装配逻辑真实可运行（本轮复跑确认）；但 demo 里的 EdgeIM 描述数据继承了污染源 A |
| `docs/MULTI_KERNEL_SYSTEM_ARCHITECTURE.md` | "生产级统一控制底座" | **AGENT_GENERATED（DRAFT 级别的设计文档）** | 架构设计本身是对四个真实外部项目机制的合理转化构想，但"生产级"措辞超出目前只有 toy 原型的证据强度；科研台职责定义（§四）继承污染源 A |
| `docs/MAINTENANCE_MANUAL.md` | "维护手册" | **SOURCE_VERIFIED**（5 项铁律定位的源码陷阱） + **DOCUMENTATION_OVERSTATES_GATE_STRENGTH**（排错矩阵里 Outcome Floor 的"拒签"描述） | 5 项铁律引用的 loopx/openviking 源码问题真实存在；但故障排查表把 Outcome Floor 描述为比源码实现更强的门禁 |
| `docs/NEXT_PHASE_EXECUTION_PLAN.md` | "下阶段演进与下周实操路线图" | **AGENT_GENERATED, PARTIALLY_MISALIGNED** | Week 1（Moraine）与 Week 3（LoopX Hooks）目标建立在 SOURCE_VERIFIED 材料上，可执行；Week 2/4（10 篇论文入库、并发死锁挖掘）建立在污染源 A/B 之上，需要先修正范围定义才能执行 |
| `MASTER_EVALUATION_MATRIX.md` | "28 仓全景总决算" | **AGENT_GENERATED**（元数据部分标 SOURCE_FACT，处置建议标 RECONSTRUCTION） | Stars/license 等结构化字段来自 `BATCH_METADATA_RECEIPT.json`（本轮未重新拉取 API 复核，NOT_SEARCHED）；五选一处置建议是基于 SOP 评分标准的合理推断，未发现���部矛盾 |
| 孙猛导师画像 | （无单一声称文件；隐含于桥接设计） | **MISSING**（不是 UNKNOWN，是确认不存在） | 全仓检索无独立画像文件；仅存在已自我标注 UNSOURCED 的交集矩阵草稿（`01_` 轨道） |
| `RESEARCH_AGENT_CONSTRAINT_v1.0.md` | "全局父规约" | **DRAFT, UNCOMMITTED** | 内容质量本身审计范围内未发现问题，但从未 `git add/commit`，对任何新分支/新 clone 不可见，不具备声称的约束力 |
| Git 分支隔离纪律执行情况 | "已单开独立分支" | **NOT_APPLIED（本轮 5 个提交前）** → **APPLIED（本审计起）** | reflog 确认 5 个 purge/audit 提交发生在 main 上；本审计已切到 `audit/redteam-external-ref-2026-09-20` 分支执行 |
