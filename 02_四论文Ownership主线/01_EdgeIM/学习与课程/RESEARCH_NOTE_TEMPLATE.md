# Research Note Template（研究笔记模板）

**目标**：用可检查证据解释数据怎样流动、状态怎样变化，以及算法步骤怎样落到代码；再把怀疑推进到可裁定、可复查的研究记录。源码行数、阅读时长和穷举式源码注释都不是理解或证据。

本模板不代替做题，也不提供任何站题答案。第一次使用前先读 [训练入口](./START_HERE.md)、[论文地图](./PAPER_MAP.md) 和 [研究地图](./RESEARCH_MAPS.md)。后续站点文件只链接本文件中已填写的选定行，不复制整套表格。

开始前先认几个词：**对象**是一次被处理的数据单位；**接口**是对象在步骤间进入或离开的边界；**状态**是处理过程中会被读取或改写、并影响后续行为的值；**算法步骤**是用输入、条件、更新和输出描述的操作；**证据**是他人能定位并复查的原文、代码、运行记录或明确推理；**claim ceiling（主张上限）**是当前证据最多允许说到哪里。

每行先分配稳定 ID：`SR-__`、`EA-__`、`EC-__` 或 `RH-__`。**provenance（来源链）**记录“原始来源 -> 核查动作 -> 本行结果”；**credit（贡献归属）**记录谁阅读、运行、推理或总结。找不到足以裁定的证据时写 `UNKNOWN`（未知），不能强行给答案。

`Epistemic Integrity`（认知诚信）要求记录 `UNKNOWN`、negative evidence（未观察、失败或反例）、来源链和贡献归属。`Research Economy`（研究经济性）要求写明检查成本与 decision impact（结果会改变哪个决定）。使用顺序是：先填 System reading（系统阅读记录）；出现主张时填 Evidence audit（证据审计）；出现待检怀疑时再填 Evidence closure（证据闭环）和 Research hooks（研究钩子）。

## 无关微例：三笔订单流水

本例只演示填表，与本学习包中的论文机制无关。输入依次为 `o1={amount:"12.50"}`、`o2={amount:"7,50"}`、`o3={amount:"10.00"}`。玩具流程先解析并校验每笔订单金额，再把有效金额加到累计总额，最后输出有效订单数与总额。

<a id="demo-code"></a>
```text
L1 total = 0; valid_count = 0
L2 for order in orders:
L3     amount = parse_amount(order.amount)
L4     validate amount >= 0
L5     total = total + amount; valid_count = valid_count + 1
L6 output valid_count, total
```

字段 `"7,50"` 的解析契约尚未给出：若逗号表示小数点，纸面总额为 `30.00`；若解析器删除逗号，纸面总额为 `772.50`。两者都是运行前推论，不是观察结果。

## System reading

System reading（系统阅读）把处理链拆成输入、接口、状态更新、算法步骤、代码位置和实际行为。data flow（数据流）是对象从输入经接口到输出的路线；state transition（状态转移）必须分别写 before（更新前）、update（更新动作）和 after（更新后）；observed behavior（观察行为）只写亲眼查看或实际运行所得；mismatch（不一致）是算法描述、代码和观察之间可定位的差别，尚未解释时不能叫 bug。

`commit` 是一次可定位的代码内容快照；`version` 是被检查制品的版本标识；`symbol name` 是函数、类或变量等代码实体的名称。exact code anchor（精确代码锚点）至少包含 commit 或 version、文件路径、symbol name，并在需要时加行号。没有运行就写 `NOT RUN`，不要把预测写成观察。

### 微例行

| ID | input / output | data flow | state before / update / after | algorithm step | exact code anchor | observed behavior | mismatch | provenance / credit | claim ceiling |
|---|---|---|---|---|---|---|---|---|---|
| <a id="demo-sr-01"></a>`DEMO-SR-01` | 输入：`o1,o2,o3`；输出：有效订单数、总额 | `orders -> parse -> validate -> accumulate -> output` | 处理 `o1` 前：`total=0`；加 `12.50`；之后：`total=12.50` | 校验金额后更新累计总额 | 本页 [`demo-code` L2-L6](#demo-code)；version：本模板微例；symbol：`parse_amount` | `NOT RUN`；只有两种纸面预测 | 尚无实际行为可比较 | 本页玩具流程 -> 纸面分支 -> 本行；模板作者完成 | 只支持数据与状态的阅读路径，不支持真实解析行为 |

### 空白可复用表

| ID | input / output | data flow | state before / update / after | algorithm step | exact code anchor | observed behavior | mismatch | provenance / credit | claim ceiling |
|---|---|---|---|---|---|---|---|---|---|
| <a id="sr-blank-01"></a>`SR-__` | ________ | ________ | before：________；update：________；after：________ | ________ | commit/version：________；路径：________；symbol/行：________ | ________ / `NOT RUN` | ________ / `NONE OBSERVED` | 来源链：________；credit：________ | 当前最多支持：________；仍为 `UNKNOWN`：________ |

## Evidence audit

Evidence audit（证据审计）检查一句主张来自哪里、怎样验证、结果是什么，以及它最多支持什么。`static reading`（静态阅读）是不执行程序而检查固定版本源码；`dynamic run`（动态运行）是在写明环境和输入后实际执行；`paper walkthrough`（论文走查）是沿页码、章节、图表或算法逐项核对原文。每行只选一个当前最直接的来源标签：

- `PAPER-TEXT`：论文作者明确写出的内容；只证明“作者这样写”，不自动证明内容为真。
- `CODE-EVIDENCE`：固定版本的源码、测试或运行输出直接展示的事实；必须注明 static reading 或 dynamic run。
- `USER-INFERENCE`：学习者依据已列证据作出的推理；须保留推理步骤和可推翻条件。
- `AGENT-SUMMARY`：AI 对材料的转述或综合；只作导航，必须回原始来源验证。
- `UNKNOWN`：来源未定位、核查未完成或现有证据无法裁定。

### 微例行

| ID | claim | evidence class | source anchor | verification action | result | provenance / credit | claim ceiling |
|---|---|---|---|---|---|---|---|
| <a id="demo-ea-01"></a>`DEMO-EA-01` | `o2` 的解析方式会改变输出总额 | `USER-INFERENCE` | 本页 [`demo-code` L3-L6](#demo-code) 与三个输入字段 | 分别代入 `7.50` 和 `750` 做纸面计算 | 得到 `30.00` 与 `772.50` 两种预测；未运行 | 玩具流程 -> 分支计算 -> 本行；模板作者计算 | 只说明解析差异会影响纸面结果；实际采用哪种解析仍为 `UNKNOWN` |

### 空白可复用表

| ID | claim | `PAPER-TEXT / CODE-EVIDENCE / USER-INFERENCE / AGENT-SUMMARY / UNKNOWN` | source anchor | verification action | result | provenance / credit | claim ceiling |
|---|---|---|---|---|---|---|---|
| <a id="ea-blank-01"></a>`EA-__` | ________ | ________ | ________ | ________ | ________ | 来源链：________；credit：________ | 当前最多支持：________；不能支持：________ |

## Evidence closure

Evidence closure（证据闭环）把怀疑转成竞争解释和能区分它们的检查。target explanation（目标解释）是本行要支持或反驳的明确对象；discriminating evidence（区分证据）是不同解释会给出不同预测的证据；precommitted decision rule（预先承诺裁定规则）是在检查前写下“哪个结果使哪个解释受支持或被反驳”；cheapest check（最低成本检查）是在足以改变下一决定的检查中成本最低的一项。残余未知是本轮后仍未裁定的部分。“看起来有 bug”本身不能关闭一行。

状态必须带对象：`OPEN(A)` 表示解释 A 尚未裁定；`SUPPORTED(A)` 表示证据支持 A；`REFUTED(A)` 表示证据与 A 的预测冲突；`BLOCKED(A)` 表示缺少数据、权限、环境或来源而无法检查 A。若结果不能区分竞争解释，两者都保持 `OPEN`。

### 微例行

| ID | suspicion | target explanation | competing explanations | discriminating evidence | cheapest check | precommitted decision rule | observation | status | residual unknown / next decision | provenance / credit | claim ceiling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| <a id="demo-ec-01"></a>`DEMO-EC-01` | `"7,50"` 会怎样进入累计总额 | A：逗号按小数点解析 | A：解析为 `7.50`；B：删除逗号后解析为 `750` | 固定三笔输入并查看 `o2` 解析值与最终总额 | 运行一次玩具实现，记录解析值和输出 | 若总额 `30.00`：`SUPPORTED(A)`、`REFUTED(B)`；若 `772.50`：`REFUTED(A)`、`SUPPORTED(B)`；报错或其他结果：`OPEN(A)`、`OPEN(B)` | `NOT RUN` | `OPEN(A)`；`OPEN(B)` | 解析契约和实际行为未知；下一步按最低成本检查运行 | 字段差异 -> 预注册规则 -> 待运行；模板作者设计 | 只能形成可区分检查，不能声称哪种解释成立 |

### 空白可复用表

| ID | suspicion | target explanation | competing explanations | discriminating evidence | cheapest check | precommitted decision rule | observation | `OPEN / SUPPORTED / REFUTED / BLOCKED` + object | residual unknown / next decision | provenance / credit | claim ceiling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| <a id="ec-blank-01"></a>`EC-__` | ________ | A：________ | A：________；B：________ | A 预测：________；B 预测：________ | 输入：________；只改：________；观察：________；成本：________ | 若 X：`SUPPORTED(A)` / `REFUTED(B)`；若 Y：`REFUTED(A)` / `SUPPORTED(B)`；其他：`OPEN(A)` / `OPEN(B)` | ________ / `NOT RUN` | ________(A)；________(B) | 残余未知：________；下一决定：________ | 来源链：________；credit：________ | 当前最多支持：________ |

## Research hooks

Research hook（研究钩子）是能被最小测试推进、并会影响决定的问题，不是研究贡献声明。assumption 是结论所依赖的条件；arbitrary design choice 是有合理替代方案却尚未说明依据的选择；uncovered failure mode 是现有测试或论证未检查的具体失败方式；guarantee-loss condition 是会使原保证前提失效的条件；minimal counterexample 是使主张失败的最小候选输入；alternative 是可比较的替代做法；minimal test 是只改变关键因素的最低成本检查；decision impact 是不同结果分别改变的决定。与问题无关的字段写 `N/A + 理由`，禁止为了填满而编造。

`formal object`（形式对象）是用明确定义的变量、集合或关系表示的研究对象；`downstream`（下游）是读取当前步骤输出的后续步骤或使用者。proof obligation（证明义务）是为了允许某个主张而必须补齐的证据，必须写成：“为允许主张 ________，必须以 ________ 证明/反驳 ________。”其 layer（层次）只先选最直接的一层；跨层结论另建行：

- `implementation`：具体源码和运行行为是否符合声明的程序、接口与状态更新。
- `model`：在写明输入和假设下，算法或 formal object 的性质是否成立。
- `abstraction`：现实对象到 formal object，或完整数据到摘要的映射，是否足以支持 downstream 主张。

### 微例行

| ID | assumption | arbitrary design choice | uncovered failure mode | guarantee-loss condition | minimal counterexample | alternative | minimal test | proof obligation | layer | decision impact | provenance / credit | claim ceiling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <a id="demo-rh-01"></a>`DEMO-RH-01` | 订单生产方与解析器使用同一金额格式 | 接受本地化字符串，而非统一的整数分字段 | 小数逗号的解析分支未测试 | 两端金额格式约定不一致 | 单笔 `{amount:"7,50"}` | 传输整数分，例如 `750` | 对原字段与整数分字段分别运行并比较金额 | 为允许主张“输出总额按业务金额解释正确”，必须以解析契约和分支测试证明/反驳 `"7,50"` 被解释为 `7.50` | `implementation` | 若契约与运行一致，限定格式并补测试；若不一致，修解析或收窄输入合同 | 微例字段 -> 候选测试 -> 本行；模板作者分析 | 只定义实现层待证事项，不证明当前实现有误或替代方案更好 |

### 空白可复用表

| ID | assumption | arbitrary design choice | uncovered failure mode | guarantee-loss condition | minimal counterexample | alternative | minimal test | proof obligation | `implementation / model / abstraction` | decision impact | provenance / credit | claim ceiling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <a id="rh-blank-01"></a>`RH-__` | ________ / `N/A + 理由` | ________ / `N/A + 理由` | ________ / `N/A + 理由` | ________ / `N/A + 理由` | ________ / `N/A + 理由` | ________ / `N/A + 理由` | 输入：________；只改：________；指标：________；裁定：________；成本：________ | 为允许主张 ________，必须以 ________ 证明/反驳 ________ | ________ | 若结果 X：________；若结果 Y：________ | 来源链：________；credit：________ | 当前最多支持：________；仍为 `UNKNOWN`：________ |

## 链接与复用规则

填写时复制空白行，给它唯一 ID，并同步设置小写锚点，例如 `SR-12` 对应 `<a id="sr-12"></a>`。后续站点文件只链接相关行，不复制定义、表头或整张表；不同节的记录用不同 ID 互相引用。每次更新继续记录失败、`UNKNOWN`、暴露条件和 credit。
