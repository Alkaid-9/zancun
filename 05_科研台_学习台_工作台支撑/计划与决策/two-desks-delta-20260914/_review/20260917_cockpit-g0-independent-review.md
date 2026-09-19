# 科研驾驶舱 G0 独立只读复核与主控处置

日期：2026-09-17。受审范围：`RESEARCH_COPILOT_G0_FREEZE.md`、驾驶舱方案、统一参考清单及TASK-009日志。review class：`SCOPED-READONLY / SAME-PLATFORM / SAME-OPERATOR-LINEAGE`。这不是异构审、外部人审、运行验收或用户接受。

## 1. 首轮结论

只读复核返回`complete`，报告1个BLOCKER、6个MUST-FIX、1个LIMITED；确认tracked/untracked、当前／历史测试、service-up／loaded-revision边界总体没有被直接混淆，15个本地文件目标存在。代理未复验三仓Git、服务、B实现或测试输出，未查外部URL、Markdown fragment渲染或范围外文件。

## 2. 发现与处置

| 发现 | 主控裁决 | 处置 |
|---|---|---|
| 双读戳未覆盖实际消费内容，却称`ATOMIC-WITHIN-OBSERVATION` | 接受BLOCKER | 来源戳加入blob／未跟踪文件hash、HTTP响应身份、生成器和配置版本；结论降为`NO-DRIFT-OBSERVED` |
| `N-A`同时表示不适用和回执源未建设 | 接受MUST-FIX | N-A只用于合同明确不适用；未建回执源改为`MISSING / NO-VALID-RECEIPT-SOURCE`且数值留空 |
| 运行门单值阶梯会掩盖loaded revision | 接受MUST-FIX | 主方案改为commit、harvest、service-up、loaded、deployed、pushed正交事实组 |
| 矩阵使用未定义复合状态且版本不足 | 接受MUST-FIX | 拆`capability_state`与`constraint_flags`，补当前权威版本；无manifest revision保持UNKNOWN |
| 当前／历史测试证据不可直接复放 | 接受MUST-FIX | 补cwd、解释器、命令、时间、commit及历史报告路径；重跑限定单测6/6 |
| 服务观察无精确时间 | 接受MUST-FIX | 定向复查8899／8878并记录`2026-09-17T01:26:25-07:00`、响应、PID、配置和revision未知 |
| G0第6项只列开放门，未裁决证据脊柱阻断性 | 接受MUST-FIX | 新增6项issue、严重度、是否阻断、处置与关闭条件矩阵 |
| R11先补身份与可维持开放继续G0的顺序矛盾 | 接受LIMITED | 改为条件式并行输入；不阻断G0，只阻断永久注册和依赖原身份的判断 |

首轮发现全部进入文档整改；在复核者重审前保持`G0-E OPEN`，不以主控自述关闭SCOPED-READONLY门。

## 3. 第二轮复核

整改后复核仍返回`complete`但不放行：4项闭合、4项部分闭合，并新增1个BLOCKER。新增BLOCKER是G0-A历史快照`c85bba4`与当前G0-E基线`e21c7e6`没有区分；部分闭合项为消费缓冲区C身份未参与A/C/B比较、两处N-A旧语义、冻结件仍残留“五门”表述、产品合同DESIGN-ONLY与实际Skill身份UNKNOWN未拆开。

主控接受这些发现：G0-A表已明确为阶段历史观察，G0-E刷新`base_commit=e21c7e6`并把最终内容身份交给限定commit；读取协议改成`A_identity == C_identity == B_identity`并优先immutable blob／revision；所有缺失语义统一为UNKNOWN／MISSING／N-A三分；状态模型改为四类判定门加正交运行事实组；Skill行只把驾驶舱产品合同标为DESIGN-ONLY，实际Skill身份和版本保持UNKNOWN。完成第三轮复核前仍不签G0完成。

## 4. 第三轮复核

第三轮未发现新BLOCKER，但仍有2个MUST-FIX，因此`SCOPED-READONLY NOT PASS`：主方案标题和绿色判定仍残留“五门”措辞；workbench任务／事件来源戳未明确内容digest、Git blob或不可变事件revision，无法执行A/C/B身份比较。

主控接受并修正：方案统一为“四个判定门＋一组正交运行事实”，绿色只由适用判定门决定，运行事实不压成PASS；workbench任务／事件identity必须使用Git blob、内容digest或不可变revision，游标只有在单调且唯一绑定消费内容时才有效。第四轮复核前仍不签G0完成。

## 5. 第四轮结论

第四轮返回`SCOPED-READONLY PASS`。第三轮剩余2个MUST-FIX均闭合，快速扫描未发现新BLOCKER或MUST-FIX；无新增LIMITED。明确确认：四个判定门与正交运行事实分离，绿色规则不消费运行事实；workbench任务／事件identity要求Git blob、内容digest或不可变revision，游标只有单调且唯一绑定消费内容时有效，并与A/C/B比较一致。

剩余OBSERVATION仅为G0-E限定commit及恢复入口当时尚待主控收口。A/B独立复核、用户试用、合同／历史证据采收和WP0原门继续开放，不由本次复核关闭。未覆盖Git最终diff／commit、服务和测试复验、workbench实现、外部链接及范围外文件；本结论不是异构审、外部人审或用户接受。
