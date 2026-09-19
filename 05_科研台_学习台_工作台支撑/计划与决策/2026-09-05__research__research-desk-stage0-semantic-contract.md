# 独立科研台阶段 0：三源语义合同

**Date**：2026-09-05  
**Status**：`PROPOSED / USER-REVIEW-PENDING / DESIGN-ONLY`  
**Parent**：[三源材料改进提案](2026-09-05__research__research-desk-three-source-improvement-proposal.md)  
**Task**：`TASK-20260905-004`  
**目的**：冻结后续只读来源库需要遵守的输入、对象、ID、状态和验收边界。  
**不包含**：导入器、数据库、UI、工作台 API、Obsidian/Reviva 私有 API 或任何自动同步实现。

## 1. 三源 manifest

阶段 0 的 manifest 是输入快照，不是知识库。每项至少保存：

| 字段 | 规则 |
| --- | --- |
| `source_id` | 稳定命名空间 ID；不因文件移动改变 |
| `origin_path` | 当时观察到的绝对路径；只用于定位，不作为身份唯一依据 |
| `source_kind` | `xlsx_workbook`、`markdown`、`pdf`、`web_capture`、`git_repo` 等枚举 |
| `content_sha256` | 原始字节 SHA-256；重新导入先比较哈希 |
| `captured_at` | 读取或捕获时间，带时区 |
| `version_label` | 文件名版本、正文版本或 `UNKNOWN`；冲突必须显式记录 |
| `authority_class` | `raw_source`、`user_note`、`external_claim`、`derived_index` |
| `locator_scheme` | `cell`、`line`、`page`、`section`、`commit` 等 |
| `import_policy` | 只读、可导出、是否允许候选抽取 |
| `supersedes` | 已知旧 source ID；未知不猜 |

三份当前输入快照：

| source_id | 来源 | SHA-256 | 盘面用途 |
| --- | --- | --- | --- |
| `src:workbook1` | `D:\\Alkaid\\Desktop\\工作簿1.xlsx` | `d28ce510bfcc3cb00b1f0ee85d89a61b99d17d1df179a5dbee46c81fd9f52f34` | 摘录、个人笔记、论文表和图片/链接的原始收件箱 |
| `src:operator-booklet-20260905` | `D:\\Edge下载\\研究操作符与横向迁移案例册.md` | `d7e8c2e826d29aca015ca00cf309ce5ec4ac8609a39a30a5d52e25e14ec36c0c` | 操作符、案例、迁移边界和证据上限 |
| `src:research-training-20260905` | `D:\\Edge下载\\科研学习与训练体系-v0.1.md` | `e917002cca1caa9fabbb62a18d4286209e38c1f767796cb67ca105a59ae6d63d` | 学习循环、七图、能力/调度/证据三轴和复测协议 |

`version_label` 的冲突：第三个文件名为 `v0.1`，正文标题为 `v0.3`。两者都保留；在用户裁定前显示为 `VERSION-CONFLICT`，不静默选一个。

## 2. 对象与转换边界

### 2.1 原始层

```text
Source
  -> SheetRecord / SectionRecord
  -> Excerpt
  -> UserNote or Observation
```

`Excerpt` 必须保留 `source_id`、`locator`、原文、上下文窗口、导入批次、抽取者和抽取时间。工作簿使用 `sheet_name + cell_coordinate`；Markdown 使用行号/章节；PDF 使用文件版本、PDF 页和印刷页（若可得）双锚点。

### 2.2 研究层

```text
Question -> Claim -> Evidence -> Relation -> MapView
                      \-> Comparison / Decision / Experiment
```

下列转换需要人为或明确规则触发：

| 转换 | 默认状态 | 必需条件 |
| --- | --- | --- |
| `Excerpt -> Note` | `draft` | 保留原文定位，并明确是个人记录还是外部摘录 |
| `Note -> Claim` | `candidate` | 写出主张主体、范围和依据；个人感想不得伪装成原文 |
| `Claim -> Evidence` | `unlinked` 或 `candidate` | 绑定来源、运行、复算或反例；没有证据就保留缺口 |
| `Evidence -> confirmed Claim` | `candidate` | 人工确认证据与主张同层、同范围，且没有已知竞争解释 |
| `Claim -> Relation` | `candidate` | 写明关系类型、方向、有效时间和来源 |
| `Operator -> TransferCard` | `draft` | 同时填写对应点、不对应点、预测和最小检查 |
| `LearningSession -> CapabilityObservation` | `observed` | 有学习者产物、提示量、反馈和范围；一次表现不生成长期结论 |

禁止的快捷转换：`AI 摘要 -> confirmed Claim`、`相似标题 -> genealogy edge`、`看过材料 -> capability PASS`、`一次成功 -> transferred`。

## 3. 稳定 ID 规则

ID 采用 `namespace:slug`，slug 由规范化标题或用户指定短名生成；同名对象用短哈希消歧。文件路径、行号和排序不能作为唯一身份。

```text
src:workbook1
excerpt:workbook1-sheet1-s12
note:edgeim-reading-001
question:edgeim-summary-sufficiency
claim:edgeim-c014
evidence:edgeim-p405-e03
operator:op-02
transfer:edgeim-agent-001
session:20260905-edgeim-001
```

对象移动位置时保留 ID，增加 `locator_revision`。内容发生变化时建立 source revision，不覆盖旧原文。删除只改变索引可见性或对象状态，不抹掉来源版本和历史关系。

## 4. 状态词典

### 4.1 研究对象

```text
draft -> candidate -> confirmed
                  -> disputed
                  -> rejected
                  -> archived
```

`UNKNOWN` 是证据状态和结论上限，不是“失败”或“待办”的同义词；它可以与 `candidate` 或 `disputed` 并存。`confidence` 只表达当前记录的置信度，不能替代来源。

### 4.2 学习记录

```text
scheduled -> open -> in_progress -> awaiting_feedback
                                  -> retest -> closed
                                             -> reopened
```

调度状态、能力表现和证据状态分开保存。推荐能力表现枚举为 `explained`、`reconstructed`、`implemented`、`changed_condition`、`counterexample`、`transferred_candidate`；它们不是自动递增等级。

### 4.3 关系字段

每条关系必须至少保存：

```text
relation_type
source_refs[]
source_version
created_by
created_at
valid_time
status
confidence
revision
```

`authored_by`、`affiliated_with`、`cites`、`extends_mechanism`、`analogous_to`、`supports`、`contradicts`、`derived_from` 不得合并成无类型的“相关”。

## 5. P0 真实问题候选

建议用 EdgeIM 验证科研台的第一条闭环，候选问题为：

> 在明确的日志特征定义和下游消费方下，什么摘要足以回答目标问题，哪些被压掉的信息会使结论变成 UNKNOWN？

它能够同时接住三份材料：

- 工作簿提供论文阅读与即时判断的原始记录格式；
- 操作符 `OP-01`、`OP-02`、`OP-07` 提供“质疑表示、重新测量、显式保存语义”的研究动作；
- 训练体系提供先手预测、证据闭合、失败更新和延迟复测的学习记录。

候选 P0 主链：

```text
EdgeIM PDF / workbook excerpt
  -> Question
  -> page-anchored Note
  -> one Claim with explicit ceiling
  -> one Evidence link
  -> one Operator selection
  -> one TransferCard draft
  -> one Map relation
  -> Markdown + JSON export
```

这个问题目前是 `PROPOSED`，不是已批准实验，也不要求现在修改 EdgeIM 训练题面。

## 6. 阶段 0 验收门

只有下列项目均有直接证据，才可进入阶段 1 的只读来源库：

1. 三份输入均有路径、SHA-256、读取时间和版本冲突说明。
2. 工作簿的工作表/单元格、Markdown 的章节/行、PDF 的页码定位规则已确定。
3. `raw_source`、`research_record`、`learning_record` 和 `derived_index` 的权威归属没有混淆。
4. `candidate / confirmed / disputed / rejected / archived / UNKNOWN` 的显示语义已确认。
5. ID 不依赖移动后的文件路径、工作表排序或 UI 页面。
6. P0 问题、对象主链和导出格式已被用户接受。
7. 任何 AI 生成内容默认进入候选层，不能覆盖原始材料或稳定记录。

阶段 0 失败时，只修订本合同；不建立数据库、不批量导入、不自动建图、不连接工作台。

## 7. 下一步

在用户确认本合同后，阶段 1 只读产物应为：

1. `sources.manifest`：三源快照和版本信息；
2. `source_index`：工作簿 Sheet/Cell、Markdown 章节/行和 EdgeIM PDF 页码导航；
3. 一个可重复的 `Excerpt` 浏览入口；
4. 导入前后哈希与差异报告；
5. 不生成 Claim、不自动建 Map、不接工作台。

