# RS-B 被引反查与OpenReview公开面

日期：2026-09-17  
任务：`TASK-20260917-001 / W1`  
状态：`SCOPED-READONLY-COMPLETE / CONTROLLER-SPOTCHECKED / PUBLIC-SURFACE-ONLY`

## 覆盖

Semantic Scholar精确DOI/arXiv citations端点11/11返回200，`limit=1000`且无分页残留；OpenAlex 11/11身份与反向查询返回200。Semantic Scholar部分identity请求触发429，不据此判零命中。

| 对象 | S2/OpenAlex总被引 | 2026-08-15后严格新增 |
|---|---:|---|
| SBTPN | 0/0 | 无 |
| PNULock | 1/2 | 无 |
| UAF | 0/0 | 无 |
| SegLock | 0/0 | 无 |
| SBPN | 1/1 | 无 |
| EdgeIM | 3/2 | 无 |
| MHP | 2/1 | 1，正文核实 |
| FoldA | 1/0 | 严格为0；存在未确认候选 |
| AgentLTL | 3/0 | 1，正文核实 |
| SAP ABM | 0/0 | 无 |
| TriCEGAR | 2/0 | 严格为0；ATLAS为08-14边界漏扫修正 |

## 严格新增

1. MHP被[*Beyond Locks and Thread IDs*](https://arxiv.org/html/2609.00246)引用，arXiv `2609.00246`，2026-08-31。正文参考文献直接链接DOI `10.1002/cpe.70203`。它扩展静态数据竞争分析，不是MAS占位者。
2. AgentLTL被[*STAGE*](https://arxiv.org/html/2608.22538)引用，arXiv `2608.22538`，2026-08-23。正文与参考文献直接引用`2607.02599`。STAGE以政策图和确定性代码控制agent流程，是运行时邻近占位，但未建立过程挖掘、alignment或多agent偏序保证。

FoldA的S2候选 *Stochastic Process Mining: Characteristics and Challenges* 在线日期为2026-07-20，且OpenAlex未确认FoldA关系，不计九月新增。TriCEGAR的[ATLAS](https://arxiv.org/html/2608.14352)发布于2026-08-14，是重要基线漏扫修正，不计九月增量。

## OpenReview 2026公开面

查询入口为OpenReview API搜索，覆盖`conformance agent`、`agent conformance`、`conformance checking`、`probabilistic model checking`、`multi-agent concurrency`、`runtime verification`、`multi-agent safety`。

- ICLR 2026声明`public_submissions=true`；目标合取未见正主，宽词只得到邻近工作。
- ICML 2026声明`public_submissions=false`，但公开API仍可见部分accepted/rejected条目；精确短语未见正主。
- NeurIPS 2026声明`public_submissions=false`，因此返回零只能写“公开面不可判定”。
- 普通forum页主控复查被challenge重定向，不绕过验证码。

此前漏扫但会收紧边界的2026正式邻居：

- [BPOP](https://openreview.net/forum?id=UAXQW194WT)：从噪声线性agent traces推断潜在依赖偏序，并与process-mining baseline比较；压缩“agent轨迹偏序发现”新颖性，不做conformance/safety。
- [GLARE](https://openreview.net/forum?id=3a8fm24EQd)：轨迹事件转LTL并编译为确定自动机用于reward shaping；不是在线alignment。
- [HyPOLE](https://openreview.net/forum?id=EVoPYB6ss3)：HyperLTL引导部分可观测MARL；不是LLM-agent过程挖掘。
- [SysMoBench](https://openreview.net/forum?id=SAeaTz8YoM)与[VERIFY](https://openreview.net/forum?id=NChBLvOr7I)：TLA+规格生成评测与LTL-NL／模型检查基础设施，属于邻域基础件。

## 判定与边界

当前公开面仍未发现“过程模型级conformance × LLM/MAS × 运行时强制”或“概率模型检查 × LLM-MAS级联”的2026顶会正主。该结论不覆盖隐藏投稿、未索引PDF正文、删除记录、匿名在审面或登录后页面。
