---
id: TASK-20260915-011
title: 两台参考续评与分批限定提交存档
date: 2026-09-15
runtime:
  model: Codex; exact SKU UNKNOWN
  effort: UNKNOWN
  effort_source: 当前平台未提供可确认的有效effort
  launch: 当前交互式会话
type: research
status: completed_with_open_gates
area: research-desk
project: research-desk
todo_ids: []
owners:
  - Codex controller
related:
  - progress/decisions/two-desks-delta-20260914/REFERENCE_EVALUATION.md
  - progress/decisions/two-desks-delta-20260914/REFERENCE_INTEGRATION_PLAN.md
---

# 目标与授权

用户明确“继续推进，记得及时commit存档，不用总等我”。在已明确的参考评估与设计范围内继续，完成可核验小批次即限定提交，不逐次请求commit许可；不自动push。此授权不扩大为安装、模型调用、真实资料接入、应用／课程改造、部署或代签用户验收。

# 当前计划与写域

1. 先将本会话两台设计基础、参考清单、方案与首轮评估作checkpoint提交，保留历史未授权／未提交记载的当时时点。
2. 补核R07/R09与摘录／返回决定相关的模型输入边界，给原段摘录候选补可审阅的窄合同，不安装运行外部工具。
3. 将实际结果回填原集中评估与入口、记录未查面及反例，再限定提交本次增量。

第一批allowlist：two-desks-delta-20260914目录现有8份设计／参考Markdown；TASK-20260914-002及TASK-20260915-008/009/010的4份本会话日志；本日志；共享INDEX只暂存上述5条任务行，不采收其他行、行尾修正或他窗改动。合计13份文档＋1份部分暂存的INDEX。不提交应用A/B代码、其回执、课程I01原件、其他共享设计、学习记录／作答或生成视图。

文档引用的旧共享输入与外部应用回执不一定都在本批Git树中；工作区链接有效不等于本commit是独立可运行镜像。它是限定文档存档，不声称A/B实现已提交。原app仓`main@d53d188faff8e64ae9d22d92dd1eeab1b8309b84`及其既有脏改动只读。

# 验收与检查

- 文档内容、UTF-8、引用目标、关键来源及边界符合实际阅读范围；当前结果与历史时点分开。
- 暂存路径严格等于allowlist；INDEX仅本会话指定行，其他工作树字节不改。
- 检查暂存diff（按原CRLF解释），提交后查实际tree与暂存区；不因commit成功声称内容／用户验收通过。
- 后续只审影响设计的发送链，不将源码声明或已有测试定义算成实测；独立复核无产物则保持开放。

# 当前事实

开工MAS为`master@f9f42db39be4286e6275ffbeb636ffae53e1f23e`，暂存区为空；文档目录尚未跟踪，共享INDEX有其他窗口增量。solver预检通过，8899 allocator签发TASK-20260915-011。用户的commit许可已生效，旧“未commit”记录保留为历史，不继续当禁令。

# 已做与未做

第一批归档已完成；第二轮限定源码核验及原段摘录窄合同已交付。R07核到客户端发送边界，R09核到实际context-engine→legacy适配器边界及定位算法；未穷尽供应商／服务端／Pi，不作全链通过声明。

已新增SOURCE_EXCERPT_PROPOSAL.md：UTF-8文本整行区间、原quote与本人正文分开、原件版本未知不伪造、窄GET、三写路径、缓存身份、返回及EXR-01–10。发现本地source缓存键缺版本／行区间、asset接口返回登记摘要，均已成为合同差异。未修改应用或真正运行EXR用例。

剩余：独立复审、真实用户试用、应用施工、R01导入恢复等未查面；OpenScience身份／享做设备仍待补。未做安装、模型调用、真实资料、课程补修、push或部署。

# 下一步

审阅SOURCE_EXCERPT_PROPOSAL的窄范围，若批准应用施工则建立独立实施任务，先核A/B工作树与实际CONTRACT_DELTA，再按EXR用例施工；不重写整体架构。用户已允许常规commit，不需每个小批次再请求。应用、安装、真实资料与push仍单列，不从存档授权推定。

# 风险与撤回

共享树只按文件／行采收，不git add -A、commit -a、reset、stash或归一化共享行尾。如并发写入改变暂存区，先核差异，不把别人的内容一并提交。撤回未来只针对本任务commit的自有文档差异，不覆盖共享文件或应用改动；本轮不执行撤销。

# 结果与提交回执

- 第一批commit：`ac87186fe447ca749a7638bd1daedc7c8212fc5a`，`docs(two-desks): archive design and reference evaluation checkpoint`。实际14路径，1620新增行；13份文档＋INDEX的5条指定任务行。提交前13文档117个本地链接通过；暂存diff检查通过，提交后暂存区为空。
- INDEX采取HEAD内容加指定行的cached patch，仅暂存本会话5行；工作树不重写，其他行及原HEAD行尾字节保留。HEAD历史混合行尾不在本次顺手修复；工作树仍保留其他窗口已有CRLF增量。未提交应用A/B、课程、其他共享旧稿或生成视图。
- 第二批交付范围：SOURCE_EXCERPT_PROPOSAL、REFERENCE_EVALUATION §9、清单／方案／两入口、本文及INDEX仅TASK-011状态行。检查后提交同一主题的窄增量；其最终commit以本文件的Git提交记录为准，避免在文档内伪造自身commit号。
- 新源码坐标与未查面集中于REFERENCE_EVALUATION §9；无代理独立证据，不重试先前429，不将静态链路或test定义算运行结果。
- 一次只读定位命令误把应用config路径放到MAS cwd，并查了不存在的旧CONTRACTS路径，返回不存在；随后用应用绝对路径和已确认RD-2正本核对，无写入或越界读取。
- 第二批文档检查通过：7份文档严格UTF-8、115个本地链接目标／行号／锚点、围栏、无乱码／尾空白、EXR-01–10齐全；scoped diff空白检查退出0。共享INDEX仅TASK-011行CAS替换，工作树保持纯CRLF；写后值`80dfdcc4f0828a4f7ab67059aba976052e4854c36996741bbcd8ea3f9adfab4d`仅用于登记保形核对。暂存时仍从HEAD构造该单行差异，不采收其余未提交行。
