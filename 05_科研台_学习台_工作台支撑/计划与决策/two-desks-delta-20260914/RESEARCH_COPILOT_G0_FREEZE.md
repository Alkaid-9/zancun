# 科研驾驶舱 G0 当前事实与语义冻结

日期：2026-09-17。任务：`TASK-20260916-009`。状态：`G0 COMPLETE_WITH_OPEN_GATES / SCOPED-READONLY-PASS`。

上游：[驾驶舱方案](RESEARCH_COPILOT_PROJECT_COCKPIT_PLAN.md)与[统一参考清单](REFERENCE_NOTES_20260915.md)。本件只冻结可追溯事实、合同依赖和显示语义，不修改应用、真实数据库、WP0隔离实现、Skills、课程、sealed、答案或生成视图。

## 1. G0-A：三仓、服务与开放门快照

G0-A Git快照观察日期：2026-09-17（America/Los_Angeles）。该表保留阶段A当时观察，不冒充G0-E当前HEAD。G0-E整改基线已于`2026-09-17T01:30:49-07:00`刷新为MAS `master@e21c7e63c589be7582217f470d95397f7c66d2fd`，其上有本件、方案、复核回执和任务日志的限定未提交整改；最终内容身份由G0-E限定commit及其diff确定。Git远端未fetch；ahead/behind仅相对本地已知upstream。服务定向复查时间为`2026-09-17T01:26:25-07:00`。

| 面 | 身份与当前状态 | 本阶段结论上限 |
|---|---|---|
| MAS 主仓 | `/mnt/d/MyResearch/MAS_Safety_Project`；`master@c85bba4401b616ced1ed33ad965abc2a7fba20e1`；相对本地`origin/master`为`+22/-0`；index为空；46个tracked change、70个untracked入口 | TASK-008设计基线已提交；共享树仍含大量他窗改动，后续只能限定路径／hunk提交 |
| research-desk | `/mnt/d/MyResearch/research-desk`；`main@0b3a54178e4ec58fb96eb8570101c44d94ac5687`；无已配置remote/upstream；index为空；tracked change为0、untracked入口61 | 已跟踪应用代码在该快照干净；A/B合同、回执及验收材料存在于未跟踪面，不等于已采收或可由commit恢复 |
| WP0隔离树 | `/mnt/d/MyResearch/MAS_Safety_Project-wb2-wp0-20260901`；`codex/wb2-wp0-20260901-root@02da69bfd54f5a2fdfb70b6ae085c1178bfea43e`；index为空；33个tracked change、17个untracked入口 | 隔离实现仍是复合脏树；历史TECH／CONTROLLER通过不关闭异构审、用户接受、精确采收、8899加载或push |
| 工作台服务 | `2026-09-17T01:26:25-07:00`请求`http://127.0.0.1:8899/api/version`返回HTTP 200：`schema_version=4`、`generated_at=2026-09-17T00:39:02-07:00`、`todo_hash=c68b...b93`、`claimed=0` | 只证明请求时服务可答；WSL `ss`未显示8899监听进程，且未核其代码revision，正式状态为`SERVICE-UP / REVISION-UNKNOWN`，不得显示“WP0已加载” |
| research-desk DEMO | `2026-09-17T01:26:25-07:00`探测首页HTTP 200；PID 8705自2026-09-16 22:29:13运行，命令使用`acceptance/user-trial-TASK-20260915-017/config.demo.json`；此前同轮`127.0.0.1:8873`不可达 | 8878是隔离用户试用入口，不是真实数据库或部署；服务存活不等于用户已试用、接受或A/B独立审通过；loaded revision未由进程自报，显示`REVISION-UNKNOWN` |

### 1.1 当前开放门

- R11继续为`IDENTITY-OPEN / SCREENSHOT-ONLY`；用户未提供可核原始身份。本任务不注册永久`research-desk` slug。
- A/B技术历史回执保留；有效独立复核、真实用户试用和未跟踪合同／回执采收仍开放。
- C04-C07、EXR及P1a/P1b、P2-P7均未由G0-A启动。
- WP0异构审、用户接受、精确采收、8899受控加载和push仍开放；当前8899 HTTP 200不能代签这些门。
- R12 `agent-stack-notes@e17d0a8edff0b01d340c385d936b5ecaca5e8178`仅为方法参考，不是已接入记忆系统。

### 1.2 G0-A停止条件与验收

本阶段只允许记录身份、状态和证据上限。若发现index非空、仓库身份漂移、服务需重启、真实库访问或归属不明差分，停止写入相应面。本次三仓index均为空，没有重启服务、运行应用测试、访问真实数据库、fetch、部署或push。

G0-A验收：三仓根、分支、HEAD、index/worktree、服务可达性及开放门均有当前观察；运行事实与加载／接受结论分离。结论为`G0-A COMPLETE`，不代表G0整体完成。

## 2. G0-B：实际B合同、实现、测试与恢复载体

### 2.1 权威合同与身份

实际B合同为 `/mnt/d/MyResearch/research-desk/acceptance/b-TASK-20260915-004/CONTRACT_DELTA.md`，SHA-256为`ec60d6bd3ae5d6cf71d8822cbe9d91fb88cde3ca1274d80ec02b544a52733cb6`。它定义goal／requirement／attempt／feedback／research_judgment、branch_origin和v2显式版本导出；旧`B_CONTRACT_PROPOSAL.md`仅是设计来源。

该合同当前仍未被research-desk Git跟踪，因此“文件存在并与当前实现可对账”不等于“合同已稳定采收”。应用代码已由`b54ea71`提交，N3在`c86f6d1`继续修改`app.js`与`b.js`，试用准备在`0b3a541`提交。驾驶舱若显示B合同状态，必须分成：`contract_present=yes`、`contract_tracked=no`、`implementation_commit=b54ea71`、`current_app_commit=0b3a541`，不得合并为一个“已冻结”。

### 2.2 当前实现对账

当前已跟踪代码仍包含合同关键机制：

- `research_service.py`保留research_judgment、固定feedback attempt revision不可删除、branch_origin验证和v2 object/view selections。
- `research_desk.py`保留goals、knowledge、requirements、research-judgments四个窄GET入口。
- `record_store.py`保留View return_context持久化；`b.js`与`test_two_desks_b.py`均已跟踪。

旧`B_SCOPED.patch`的SHA-256为`2116a3ded4e8e7ba92963d905f962d354724ef1bd36f6df24c90629b76dd5f6e`。它在B交付时曾通过reverse check；对当前`0b3a541`重做`git apply --reverse --check`失败，冲突位于随后继续修改的`app.js`和`b.js`。因此该patch只证明B开工快照到当时交付的hunk归属，不能证明当前整文件与旧patch字节相等；当前实现身份应以提交链和现行测试为准。

### 2.3 测试口径

- 本轮先在`/mnt/d/MyResearch/research-desk`按错误模块路径调用`/home/alkaid/miniconda3/envs/solver/bin/python -m unittest app/tests/test_two_desks_b.py -v`，被环境中的第三方`app.py`抢占并在Nougat／Albumentations导入阶段失败；没有进入B测试。输出保留在当前会话工具回执，未另造日志文件；不算产品RED，也未改环境。
- 先按仓库要求在MAS根用显式solver环境运行`bash tools/scripts/require_solver_env.sh`通过；随后于`2026-09-17T01:26:25-07:00`至`01:26:26-07:00`在research-desk `main@0b3a541`运行`/home/alkaid/miniconda3/envs/solver/bin/python -m unittest discover -s app/tests -p 'test_two_desks_b.py' -v`：6/6通过，0.570秒。执行前后应用tracked worktree均干净；验收材料仍有未跟踪项。
- B浏览器27/27、A回归38/38、C03回归22/22和后端28/28来自2026-09-15历史报告，受测基线及后来采收关系见`b54ea71`。证据分别位于`acceptance/b-TASK-20260915-004/run-05/b-browser-report.json`、`a-regression/run-02/a-browser-report.json`、`c03-final/run-01/c03-browser-report.json`及`backend-final.log`；本阶段只核文件与摘要存在，没有重新运行浏览器、全后端或真实试用。
- 当前8878服务仍由TASK-017隔离配置运行；本阶段没有重启或把测试指向该服务。

### 2.4 恢复与重审触发

恢复链为MAS任务日志→实际合同→B回执→RUN_CHECKS→应用提交链；合同本体未跟踪这一缺口必须显式显示。以下任一变化触发本方案§3.3／§4及G0-C矩阵重审：合同字段／枚举改变、research_judgment或branch_origin语义改变、v2导出范围改变、实现commit移动但没有相应合同对账、合同被采收至新路径。

G0-B结论为`CONTRACT-PRESENT / CONTRACT-UNTRACKED / IMPLEMENTATION-COMMITTED / CORE-UNIT-6-PASS / HISTORICAL-BROWSER-EVIDENCE`。这不关闭独立复核、用户试用、合同采收或整体schema门。

## 3. G0-C：需求、动作、对象、正本、消费者与门矩阵

`capability_state`固定为：`EXISTING`已存在可回源能力；`PARTIAL`仅覆盖窄切片；`DESIGN-ONLY`有驾驶舱产品合同或候选机制但无产品闭环；`MISSING`设计要求存在但所需对象或回执尚未建设；`UNKNOWN`身份／事实不足；`N-A`仅指合同明确本范围不适用。`constraint_flags`另列身份或运行限制，不与状态词拼成新枚举。矩阵中的“退出门”是该行可被驾驶舱标为已接受的最低条件，不是G0本身的完成声明。

| 截图承诺／需求 | 用户动作 | 现有对象与唯一正本 | 驾驶舱消费者 | capability_state | constraint_flags | 进入门 | 退出门 |
|---|---|---|---|---|---|---|
| 项目台／课题卡 | 选择项目、问题与当前工作区 | research-desk Topic／Question／Workspace及revision；项目注册卡仍缺 | P1项目头、阶段摘要 | `PARTIAL` | `IDENTITY-OPEN` | 已选稳定Question／Workspace；项目slug需另批注册 | 每个值可回revision；未知显示UNKNOWN；用户确认项目身份 |
| 资料与证据 | 登记来源、定位原段、保存记录并回链 | source catalog、SourceRef、Object／Revision；A窄切片；EXR仍未施工 | P1资料计数与证据链接，P2摘录 | `PARTIAL` | `EXR-OPEN` | 来源身份和版本可读；非保护材料 | 来源／锚点／版本可回源；缺历史字节不冒充复现；A独立审与用户门按范围关闭 |
| 研究路线／下一门 | 查看当前问题、任务、开放门和下一动作 | research-desk对象；workbench task／CURRENT／EVENTS；C04-C07合同 | P1阶段卡与人工待办 | `PARTIAL` | `MANUAL-ONLY` | 跨仓身份和观察时间齐全 | 不建第二任务库；任务状态、研究判断和用户接受分栏；自动桥仍受WP0门约束 |
| Idea评估 | 固定idea版本，查看缺陷、反例、未知并作决定 | 驾驶舱方案点名`idea-evaluator`，实际Skill路径／版本／许可未在G0固定；决定仍归用户和内容正本 | 阶段02 | `DESIGN-ONLY`（产品合同） | `SKILL-IDENTITY-UNKNOWN / NO-RUN-RECEIPT` | idea身份、目标场景、Skill身份和运行授权 | 有效运行回执、产物回链、独立复核及用户采用／不采用决定；评分不自动排期 |
| 文献调研 | 定范围、检索、核引、记录已查／未查／不可达 | 来源目录与C04合同；方案点名`deep-research`但实际Skill身份未固定；EXR待施工 | 阶段03 | `DESIGN-ONLY`（产品合同） | `SKILL-IDENTITY-UNKNOWN / EXR-OPEN` | 问题、范围、来源政策、停止条件 | 关键主张可回来源；搜索边界和零命中上限明确；无伪造全球空白 |
| 论文蓝图 | 建章节角色、核心判断、证据与缺口 | 当前文件正本；方案点名`tech-paper-template`／`paper-writer`但实际Skill身份未固定；P5 kind合同未冻结 | 阶段04、后续章节消费者 | `DESIGN-ONLY`（产品合同） | `SKILL-IDENTITY-UNKNOWN / P5-CONTRACT-OPEN` | 问题与证据基线可用 | 蓝图身份、版本、证据ID和开放缺口可回源；作者确认结构 |
| 章节写作 | 选择蓝图段落和证据，保存／采用版本 | 文件正文正本；拟复用Object／Revision作身份目录；P5合同待定 | 阶段05、审查与导出 | `MISSING` | `PRODUCT-LOOP-MISSING` | P5冻结kind／locator／version／作者采用 | 事实强度不超证据；AI草稿与作者版分开；采用者和依据版本明确 |
| 图表整稿 | 绑定数据／代码／来源、生成图和图注 | 文件资产；方案点名`figure-designer`／drawio相关Skill但实际身份未固定；资产合同未接 | 阶段06、章节与导出 | `DESIGN-ONLY`（产品合同） | `SKILL-IDENTITY-UNKNOWN / ASSET-CONTRACT-OPEN` | 图意图、真实数据／结果、目标正文明确 | 图版本、数据／代码／来源和正文引用可复核；无虚构数据；用户采用 |
| 投稿审查 | 固定候选稿和目标场合，处理分级发现 | 文件稿件；方案点名`pre-submission-reviewer`但实际Skill身份未固定；workbench评审门待接 | 阶段07 | `DESIGN-ONLY`（产品合同） | `SKILL-IDENTITY-UNKNOWN / REVIEW-LINK-OPEN` | 候选稿版本与审查范围固定 | BLOCKER为零；处理决定和未关闭项保留；自查、独立审和用户投稿决定分开 |
| 正式导出 | 选择采用版本与格式，独立打开产物 | research-desk v1/v2 JSON／Markdown选择导出；投稿包未实现 | 阶段08、外部读者 | `PARTIAL` | `SUBMISSION-PACK-MISSING` | 被采用版本及包含／省略范围明确 | 只含明确选择；外部依赖和省略项可见；独立读取通过；用户确认正式版本 |
| 科研Skills／运行次数 | 查看可用Skill及其限制，按授权运行 | WP-S `SKILL-MANIFEST`待生成；有效运行回执合同未冻结 | P1目录、阶段技术证据 | `MISSING` | `NO-VALID-RECEIPT-SOURCE` | S1 manifest、许可、Skill版本；单次运行另有授权 | 目录／EVENTS引用／有效运行三口径分开；回执绑定task、输入版本、产物和失败 |
| 在Codex中打开 | 读取交接，在已授权窗口继续 | handoff、task log、commit和人工恢复链 | P1人工入口 | `EXISTING` | `MANUAL-ONLY` | 当前交接可读且任务身份一致 | 新窗口完成恢复绑定并核仓库；不称自动派发或自动回传 |
| 原始资料数、Skill运行数、人工待办、下一门 | 查看可解释计数及来源 | 分别来自来源目录、未来有效运行回执、workbench任务和门矩阵 | P1顶部指标 | `PARTIAL` | `RUN-COUNT-MISSING` | 每项定义、查询范围、快照版本和缺失语义冻结 | 数值均可回源；无回执源显示MISSING且留空；跨仓漂移显示NON-ATOMIC |

矩阵当前权威版本：G0-E整改`base_commit=e21c7e6`，本件及方案是该基线上的限定工作树内容，最终由G0-E commit固定；research-desk对象／B实现版本为`0b3a541`，WP0观察版本为`02da69b`。`DESIGN-ONLY`只描述驾驶舱产品合同；各Skill实际身份只定位到方案§4所列名称，manifest revision尚不存在，因此`skill_identity=UNKNOWN`且`source_version=UNKNOWN`，不得补猜路径、许可或版本。

### 3.1 权威与消费规则

1. research-desk只负责研究对象、来源、版本与关系；workbench只负责任务、授权、CURRENT／EVENTS、评审和接受；学习台只负责本人尝试、帮助条件、反馈、复测和能力证据；WP-S只负责Skill身份及许可；用户负责正式采用。
2. 驾驶舱是只读消费者，不反写研究结论、课程PASS、任务完成或作者采用。一个对象可被多阶段引用，但阶段卡不是新正本。
3. 状态模型直接采用方案§3.3：输入、技术、独立评审、用户四类判定门，加一组正交运行事实（local、commit、harvest、service-up、loaded、deployed、pushed及各自revision）。`completed`、Skill进程结束、文件存在、service-up或计数非零均不能代签。
4. G0-C冻结的是映射与判定条件；所有`DESIGN-ONLY`、`MISSING`和`UNKNOWN`必须原样进入后续UI，不用占位绿灯掩盖。

G0-C验收：R11可见承诺均有用户动作、对象、正本、消费者、当前状态及进入／退出门；八阶段与八层／七图、C包、WP包没有合并命名。结论为`G0-C COMPLETE`，不表示任何DESIGN-ONLY或MISSING能力已实现。

## 4. G0-D：跨仓新鲜度、非原子读取与失败语义

### 4.1 来源戳与快照协议

驾驶舱不拥有跨MAS、research-desk、WP0或服务的事务边界。每次构建只形成“有界观察快照”，每个输入必须带来源戳：

| 来源类型 | 必需来源戳 |
|---|---|
| Git文件 | repo根、相对路径、HEAD、index/worktree状态、文件是否tracked、实际消费字节身份、观察时间；tracked文件用Git blob ID，未跟踪文件按G0合同要求记录SHA-256 |
| research-desk对象 | 数据根身份、object/view ID、revision、kind、观察时间；若来自服务再记服务配置身份 |
| workbench任务／事件 | task_id、正本路径、文件Git blob／内容digest或不可变事件revision、schema版本、观察时间；事件游标仅在单调且唯一绑定所消费内容时可充当identity |
| Skill manifest／运行回执 | skill_id、Skill版本、manifest revision；运行另带task_id、输入版本、产物和结束状态 |
| HTTP服务 | URL、完整version响应身份（ETag／响应摘要或内容digest）、生成时间、观察时间；端口存活与代码revision分开 |
| 生成器／解析器 | 代码commit或文件内容身份、配置版本、输入schema版本；任何一项未知则输出UNKNOWN |

构建顺序固定为：读取来源身份A→按该身份读取实际消费缓冲区并现场计算`C_identity`→再次读取来源身份B→仅在`A_identity == C_identity == B_identity`时生成`NO-DRIFT-OBSERVED`静态结果。Git来源优先按immutable blob读取；对象优先按固定revision读取。任一来源不支持固定读取、身份不相等、变化、消失或无法复读，停止正常生成并输出失败摘要；不得沿用一半新值和一半旧值。该标签只表示本次消费内容与前后身份一致，不宣称跨仓原子事务；外部状态发生ABA但消费内容身份一致也不升级该结论。

### 4.2 新鲜度状态

| 状态 | 判定 | 显示与允许行为 |
|---|---|---|
| `CURRENT` | 当前来源戳与页面记录完全一致 | 显示值、来源、revision／commit和观察时间；仍不代签门 |
| `STALE` | 来源仍可读，但已知revision／commit／事件游标晚于页面 | 显示旧值和新来源身份；禁止把旧绿色当当前结论 |
| `NON-ATOMIC` | 同次构建前后来源戳不同，或依赖组合来自不一致快照 | 不发布正常计数或阶段摘要；列出漂移来源并要求重建 |
| `UNKNOWN` | 身份、版本、路径、解析语义或正本归属不足 | 显示缺失原因和恢复条件；不猜值 |
| `ERROR` | 已知来源应可读但读取／解析失败 | 显示错误阶段和来源，不回退到缓存冒充当前 |
| `N-A` | 合同明确该项目／阶段不适用 | 显示不适用原因；设计要求存在但回执源尚未定义时必须用`MISSING`，数值留空 |

时间阈值只能作为提醒，不能单独决定CURRENT。文件刚生成但引用旧revision仍是STALE；很久未变但来源戳一致可显示CURRENT并同时展示观察时间。R12的增量水位线只作为未来优化参考，G0不新增同步服务、后台监听或记忆库。

### 4.3 失败显示与停止条件

| 失败场景 | 必须显示 | 禁止行为 |
|---|---|---|
| repo根／HEAD与配置不符 | `UNKNOWN-REPO`及实际根／HEAD | 按cwd或同名目录继续 |
| tracked合同缺失但工作树有文件 | `PRESENT-UNTRACKED` | 称合同已稳定冻结或可由commit恢复 |
| 服务HTTP可达但代码revision未知 | `SERVICE-UP / REVISION-UNKNOWN` | 称WP0已加载或已部署 |
| 解析失败／字段枚举未知 | `ERROR`与字段／来源 | 静默忽略、映射到默认绿色 |
| 同次读取来源漂移 | `NON-ATOMIC`与A/B来源戳 | 发布混合快照、重用旧计数 |
| 运行回执源不存在 | `MISSING / NO-VALID-RECEIPT-SOURCE`，数值留空 | 显示N-A或0；用Skill目录数、EVENTS引用数或进程退出数代替 |
| completed但review失败／用户未验收 | 同显`TECH-PASS / REVIEW-RED或OPEN / USER-OPEN` | 压成一个PASS |
| 来源历史字节缺失 | `HISTORICAL-BYTES-UNAVAILABLE` | 用当前原文冒充当时原文 |
| 权限、license或sealed边界不明 | `BLOCKED`及所需决定 | 读取、复制、发送或索引材料 |

构建必须停止而非降级继续的条件：仓库身份错配；正本有多个竞争版本且无裁决；来源在身份A／消费C／身份B之间不一致；将要读取sealed／真实库但无授权；将要把未跟踪合同称作稳定正本；任何写入会越过G0只读边界。单个非关键字段缺失可生成失败摘要，但该字段及依赖它的计数／阶段必须按定义保持`UNKNOWN`、`MISSING`或`N-A`；设计要求存在但来源未建时必须为`MISSING`。

### 4.4 重建与恢复

失败后保留上一份静态页面及其来源戳，只标为STALE，不覆盖成“最新”。修复身份或来源后从头重读，不从中间续拼；相同输入内容身份、生成器版本与配置版本应生成语义相同的状态和链接。退出驾驶舱不影响各正本，删除派生页不删除任务、对象、回执或用户产物。

### 4.5 证据脊柱开放项裁决

| issue | severity | blocks-evidence-spine | 当前处置 | 重开／关闭条件 |
|---|---|---|---|---|
| `G0-ISSUE-A-REVIEW`：A完整独立复核无有效终态 | `MUST-FIX` | 不阻断G0语义冻结；阻断A显示为独立审通过及P1a用户价值结论 | 保持`REVIEW-OPEN`，只显示历史技术回执 | 有固定revision、范围、方法和未查面的有效独立回执；发现经主控处置 |
| `G0-ISSUE-B-REVIEW`：B两次代理无有效终态 | `MUST-FIX` | 同上 | 保持`REVIEW-OPEN`；本轮6/6单测不代替独立审 | 同A；429／中断／空回执无效 |
| `G0-ISSUE-USER-TRIAL`：A/B/C03真实试用开放 | `MUST-FIX` | 不阻断G0；阻断P1a前置和任何USER-ACCEPTED | 8878只作为隔离入口，未代签 | 用户完成最短非保护路径并明确接受／修改／停放 |
| `G0-ISSUE-B-CONTRACT-HARVEST`：实际合同未跟踪 | `BLOCKER`（稳定恢复） | 不阻断G0记录现状；阻断称合同稳定冻结和依赖它的产品施工 | 显示`PRESENT-UNTRACKED`，固定路径与hash | 经归属审阅后精确采收合同／回执，记录commit与回滚；或正式迁移并更新全部引用 |
| `G0-ISSUE-HISTORY-HARVEST`：历史证据未完整采收 | `MUST-FIX` | 阻断完整证据脊柱声明；不阻断窄G0矩阵 | 保留欠账，不扩大为本包采收 | 明确清单逐项采收／分类不可采收，并有恢复回执 |
| `G0-ISSUE-WP0`：异构审、接受、采收、加载开放 | `BLOCKER`（自动桥） | 阻断P6自动接驳，不阻断人工交接或G0 | 保持N3`MANUAL-ONLY` | 原WP0治理线各门分别关闭并绑定revision |

G0-D验收：来源戳、双读协议、六种新鲜度状态、九类失败显示、硬停止条件和重建规则均已冻结。结论为`G0-D COMPLETE`；尚未实现生成器，也未证明实际跨仓读取性能。

## 5. G0-E：主控验收、独立复核与结论

### 5.1 主控验收

| 验收项 | 结果 | 证据上限 |
|---|---|---|
| 三仓与服务事实 | PASS | G0-A阶段快照及G0-E基线刷新；未fetch、未重启、loaded revision未知 |
| 实际B合同与实现 | PASS-WITH-OPEN-HARVEST | 合同路径／hash、提交链、当前6/6单测；合同仍未跟踪，浏览器数字仍是历史证据 |
| 需求与权威矩阵 | PASS | R11承诺逐项映射；产品合同状态与实际Skill身份分开 |
| 新鲜度与非原子语义 | PASS | A/C/B内容身份、`NO-DRIFT-OBSERVED`、UNKNOWN／MISSING／N-A、失败与停止规则冻结 |
| 证据脊柱开放项 | PASS-AS-DISPOSITION | 六项均有严重度、阻断范围、处置和关闭条件；未假装问题已解决 |
| 范围 | PASS | 未修改应用、数据库、WP0、Skills、课程、sealed、答案或生成视图；未部署、push或注册slug |

### 5.2 独立只读复核

同一平台、同一操作者谱系的只读复核经历四轮：首轮1 BLOCKER／6 MUST-FIX／1 LIMITED；第二轮新增1 BLOCKER且4项部分闭合；第三轮剩2 MUST-FIX；第四轮结论为`SCOPED-READONLY PASS`，没有剩余BLOCKER、MUST-FIX或新增LIMITED。完整发现与主控处置见[_review/20260917_cockpit-g0-independent-review.md](./_review/20260917_cockpit-g0-independent-review.md)。

该PASS只覆盖指定文档的权威归属、语义一致性和证据上限，不是异构审、外部人审、应用运行验收或用户接受。复核者未复验Git、服务、测试、workbench实现或外部链接；主控已独立执行限定Git／服务观察和B单测，但没有把两者合并成更高级审计。

### 5.3 G0完成上限

G0完成条件已满足：可见能力有权威归属或明确UNKNOWN，B实际合同依赖和未跟踪状态已钉住，八阶段／八层／七图／C包／WP包未混名，跨仓内容身份、新鲜度、非原子读取、失败显示和停止条件已冻结。结论仅为`G0 COMPLETE_WITH_OPEN_GATES`。

仍开放：R11身份、永久project slug、A/B独立复核与用户试用、B合同采收、历史证据采收、EXR、C04-C07、WP0异构审／接受／采收／加载，以及P1a/P1b和P2-P7全部施工。G0完成不授权这些工作，也不证明产品已完成。

## 6. 后续阶段

- 下一合法候选是按方案前置先完成现有C03/A/B最短用户路径观察，再由用户决定是否另行授权P1a静态验证件；G0本身不自动启动P1a。
