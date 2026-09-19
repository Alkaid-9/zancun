# IND-1 agent可观测性与护栏产品最小扫描

日期：2026-09-17  
任务：`TASK-20260917-001 / W1`  
状态：`SCOPED-READONLY-COMPLETE / CONTROLLER-SPOTCHECKED / NO-PRODUCT-TEST`

## 判定口径

- `established`：官方资料直接描述该能力。
- `partial`：只有局部trace、事后告警、请求日志或相邻产品能力。
- `not established`：本轮所查官方公开面没有直接证据，不等于能力不存在。
- “过程模型级conformance”要求比较实际执行trace与显式参考／过程模型，并产生alignment、deviation、fitness或等价conformance结果。

所有来源访问日均为2026-09-17。证据等级均为B：官方文档／官方仓库的能力自述；本轮没有独立产品实测，不能升为A。

## 产品矩阵

| 产品 | Trace采集 | 干预／护栏 | 过程模型级conformance | 官方来源 |
|---|---|---|---|---|
| LangSmith | established：生产agent traces | partial：automation、告警、webhook，未建立请求内阻断 | not established | [Observability](https://docs.langchain.com/langsmith/observability)、[Automations](https://docs.langchain.com/langsmith/rules) |
| Langfuse | established：请求、LLM、检索、工具与自定义逻辑 | not established：以观测和事后评估为主 | not established | [Tracing](https://langfuse.com/docs/observability/overview)、[Security & Guardrails](https://langfuse.com/docs/security-and-guardrails) |
| Arize Phoenix | established：OTel/OTLP多步骤trace | not established：annotation/evaluation未证明inline阻断 | not established | [LLM Traces](https://arize.com/docs/phoenix/tracing/llm-traces) |
| W&B Weave | established：conversation、turn、tool、sub-agent trace | not established：Signals对已保存turn评分／标记 | not established | [Agent tracing](https://docs.wandb.ai/weave/guides/tracking/trace-agents)、[Signals](https://docs.wandb.ai/weave/guides/tracking/view-agent-signals) |
| Datadog | established：workflow、agent决策与步骤trace | partial：扫描、脱敏、告警和路由，未证明请求内阻断 | not established | [Overview](https://docs.datadoghq.com/llm_observability.md)、[Automation](https://docs.datadoghq.com/llm_observability/configure/automation_rules) |
| OpenTelemetry GenAI | partial：定义agent/workflow/tool span，标准本身不存储 | not established | not established：telemetry schema不是conformance analyzer | [GenAI conventions](https://github.com/open-telemetry/semantic-conventions-genai) |
| NVIDIA NeMo Guardrails | established：rails、flow execution与LLM calls | established：input/retrieval/dialog/execution/output rails可阻断或修改 | not established：Colang flow不等于trace-model alignment | [Overview](https://docs.nvidia.com/nemo/guardrails/about-nemo-guardrails-library/overview)、[Tracing](https://docs.nvidia.com/nemo/guardrails/observability/tracing) |
| Guardrails AI | partial：Guard、validator和LLM调用telemetry | established：exception、reask、fix、filter、refrain | not established | [Telemetry](https://guardrailsai.com/docs/concepts/telemetry)、[Remediation](https://guardrailsai.com/docs/concepts/error_remediation) |
| Lakera / Check Point | partial：Guard logs；Red可追tool call/result | established：实时筛查并可阻止调用或返回替代响应 | not established | [Quickstart](https://docs.lakera.ai/docs/quickstart)、[Tool tracing](https://docs.lakera.ai/docs/red/trace-agent-tools) |
| AWS Bedrock Guardrails | partial：guardrail指标；完整步骤trace在Agents/Flows相邻产品 | established：过滤、阻断、mask和拒绝主题 | not established：逻辑规则校验不是过程trace conformance | [Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)、[Agents trace](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) |

汇总：trace为6项established、4项partial；运行时干预4项established、2项partial；10项公开面均未建立过程模型级conformance语义。

## 判定

原动机句判为 **partial**。可安全使用的表述是：

> 截至2026-09-17，在所查十项官方公开资料中，主流方案已分别覆盖agent/workflow tracing与运行时护栏干预；尚未建立将实际agent执行轨迹与显式过程模型进行alignment、deviation或conformance checking的公开产品语义。

出现官方文档、官方代码或可复现实测，明确把实际执行轨迹与BPMN、Petri net、XES、声明式约束或等价参考过程模型对齐并输出偏差／适应度时，必须改判。

## 未覆盖

认证后UI、企业私有文档、闭源实现、支持工单、路线图和真实运行效果未查。Guardrails AI的官方`llms.txt`返回404，其索引外表面保持UNKNOWN。不能把本报告外推为“业界绝对没有”。
