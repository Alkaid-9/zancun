# 首批 B：接口与记录约定提案

任务：`TASK-20260914-002`。状态：`PROPOSED / NOT-FROZEN / NO-IMPLEMENTATION`。本件细化[首批方案](FIRST_BUILD_PLAN.md)，不替代已有 RD-2 合同，也不是施工回执。返回[总入口](README.md)。

## 1. 本次收敛的选择

1. 复用 Object／Revision，不新建数据库；增加有明确编辑、查询和导出行为的 `goal / requirement / research_judgment` 三种记录。
2. 学习反馈继续使用 Feedback；研究判断单独保存。本人成功、提示后成功和研究主张成立不相互自动推出。
3. 补学分支引用原问题和知识的同一身份；返回原工作区后再保存研究判断，不复制一个“学习版问题”。
4. 新返回信息放在 `return_context.branch_origin`，不重新解释旧 `view_id`；回原位置不等于回滚原内容。
5. 增加显式版本选择的导出方式；旧调用保持原语义，新方式不默认导出所有视图或引用正文。

这些是推荐约定，须随 B 范围批准；当前没有修改应用合同、代码、配置或数据。

## 2. 代码实况与必须补的点

应用核对基线：`research-desk/main@d53d188faff8e64ae9d22d92dd1eeab1b8309b84`。本次只读，不运行应用或测试。

| 现状依据 | 对本批的具体影响 |
|---|---|
| [research_service.py:156](/mnt/d/MyResearch/research-desk/app/research_service.py:156) `create_object` 接受通用 kind／attrs；`update_object:347` 与 `create_workspace_entry:548` 各有写路径 | 新 kind 不能只补创建入口。三处均须遵守相同记录语义；原“正文或来源至少一个”继续有效 |
| [research_service.py:568](/mnt/d/MyResearch/research-desk/app/research_service.py:568) Feedback 的 attempt_ref、条目的 question_ref 须属于当前工作区 | 分支创建时引用原 Q、K 作为成员，不复制对象；反馈仍指分支内的真实 Attempt，不绕开原约束 |
| [app.js:678](/mnt/d/MyResearch/research-desk/app/static/app.js:678) `p1SummaryView` 选择最近更新的视图；`p1InitializeWorkspace:1085` 沿用此选择 | 返回须显式指定原视图，不能只调用原 `openP1Workspace(id)` 后宣称已恢复 |
| [research_service.py:439](/mnt/d/MyResearch/research-desk/app/research_service.py:439) 返回字段有白名单；[research_desk.py:1217](/mnt/d/MyResearch/research-desk/app/research_desk.py:1217) Object／View 已可按 revision 读取 | 可复用历史读取，但新返回结构、UI 选择和源位置恢复仍须实现；工作区聚合接口当前只取成员最新版本 |
| [research_service.py:613](/mnt/d/MyResearch/research-desk/app/research_service.py:613) 导出只接收 selected_refs／formats，取当前对象，选工作区时带全部视图；external_refs 只枚举四类字段 | 现导出不足以兑现指定历史版本、目标／尝试引用清单及显式视图选择，须补窄接口，而非只加 UI 文案 |

## 3. 记录与版本：推荐字段

沿用 `id / kind / title / body_md / author / source_refs / revision / revision_note`。表中新增字段放 attrs；`body_md` 保留该记录的说明，不允许只写 attrs 绕过原内容要求。没有正式关联的想法仍先存普通草稿。

| 记录 | attrs 的候选约定 | 用户能看见的语义 |
|---|---|---|
| goal | `category`：exam 或 research；`scope_status`：user_specified／source_checked；可选 `target_month`，来源沿 SourceRef | 首批可分别建四科目标与鲁侧目标；四科时间为用户指定 2027-12，未核章目不显示全覆盖；这不是默认排期 |
| requirement | `goal_ref / goal_revision`、`knowledge_ref / knowledge_revision`；`minimum_md / normal_md / long_term_md`；`status`：proposed／confirmed | 每份正式要求绑定一个目标和一项内容。正文深度按目标解释；暂缺的档位可留空但显示未定义，不算已覆盖；确认要求不等于本人达标 |
| attempt | 保留 `assistance`；可选 `participants / input_context`；关联要求时保存 `requirement_ref / requirement_revision`；新重做可存 `previous_attempt_ref / previous_attempt_revision` | 帮助未填显示未知，author=human 不证明独立。新题、重做和输入条件可辨，不复写旧尝试 |
| feedback | 保留 `attempt_ref`；B 新建时补固定的 `attempt_revision`；若评价针对要求，保存 `requirement_ref / requirement_revision`；正文记录评价及条件 | 评价对准当时产物和要求。反馈也可被更正；不新增第二套学习成绩权威，不自动写课程 PASS |
| research_judgment | `question_ref / question_revision`；`evidence_refs` 为 `{object_ref, revision, reason_md}` 列表；`evidence_state`：unverified／insufficient／supported／counterevidence／not_applicable | 正文说明主张和条件；来源沿 SourceRef，reason_md 解释证据用途。证据状态由明确判断记录，不按引用数量自动计算，不冒充正式 supports 边 |

版本规则：

- `*_ref` 用于找同一对象；`*_revision` 固定实际使用的内容。引用旧版本不要求它仍是最新；更新被引用对象不改旧证据。
- 新关联记录的引用版本须实际存在；旧记录未保存版本就显示“旧记录未固定版本”，不回填为当前版。
- 改要求、反馈或研究解释均生成原对象的新 revision；`revision_note` 说明修订原因。改解释不删原 Attempt，旧版可回查。
- `supported` 仅指所写条件下的当前判断，不是一般正确性证明；个人反馈与研究判断可以引用同一产物但分别更正。
- 不把这些记录强塞入当前七类正式关系，也不在本批冻结整个多层网络的数据模型。

## 4. 读写入口及分支归属

| 动作 | 推荐入口／行为 |
|---|---|
| 录入目标、要求、研究判断 | 复用 POST `/api/research/objects`；在工作区留条目继续用 `/workspaces/{id}/entries`；新 kind 的约定同时适用于两入口及 PUT 更新 |
| 找目标与要求 | 增加窄 GET `/api/research/goals`、`/api/research/requirements?goal_ref=...`；复用现有存储读取，返回真实记录，无自动进度聚合 |
| 找原问题下的判断 | 增加窄 GET `/api/research/research-judgments?question_ref=...`；列出当前记录，历史由已有 Object revision 入口读取 |
| 修改内容 | 继续携带当前记录的 expected_revision；引用的历史版本与此次写入的并发版本是两件事，不混用 |
| 进入补学 | 分支 Workspace 的 object_refs 引用原 Q、K；中心选 K；可加原专题引用，分支 View 保存 branch_origin |
| 保存尝试、反馈 | 分支 Attempt 可以关联该分支内的同一 Q；Feedback 关联分支内 Attempt。已有工作区成员限制继续成立 |
| 返回后的研究判断 | 回原问题的工作区保存 research_judgment，引用分支产物的实际版本；evidence_refs 是依据引用，不把该产物复制到原工作区 |

正式要求需要目标与知识两端都明确；未成形的捕获仍只需正文或来源。给同一目标和知识写出多个候选要求时，列出各自状态／版本，不能静默拼成一份或用最近时间推定哪个已获确认。

## 5. 返回上下文：恢复位置，不撤销后来的工作

保留旧 return_context 所有字段的原读法，新增一个 `branch_origin` 对象；新 B 分支写它，旧工作区不用迁移。其候选子字段为：

| 子字段 | 内容 |
|---|---|
| workspace_ref | 原 Workspace 的 `{id, revision}`，用于身份及当时状态核对 |
| view_ref | 原 View 的 `{id, revision}`；不能填分支自己的 view |
| question_ref | 原问题的 `{id, revision}` |
| source_ref | 一份已有支持的完整 SourceRef 或 null；整份来源不假装定位到了某段 |
| center_ref / selected_ref | 当时中心与选择的对象 ID 或 null |
| filter | 原入口当时可用的筛选值；无筛选用空对象，不生成未知筛选条件 |
| resume_note | 原问题的继续点；分支自己的学习继续点仍属于分支 View |

`branch_origin` 及上述子字段须在服务约定中明确验证；不能仅扩白名单后接受任意 JSON。正整数 revision 只用于有版本的引用，不把旧字段改成另一种含义。

往返顺序：

1. 离开前处理原页面未保存输入；明确保存成功才固定返回位置，失败保留输入并停在原处。用户可取消开分支。
2. 分支复用 Q／K 身份，保存自己的尝试、反馈和继续点；暂放后重开仍保留原返回对象。
3. 返回时显式指定原 Workspace 和 View；读取固定的 Q／View 版本作核对，不能再次默认取最近更新视图。
4. 原工作已变更时显示“原内容已有更新”；用户可查看当时引用版，或继续最新内容。编辑最新内容使用最新 expected_revision，不自动把旧视图或旧正文写回覆盖。
5. 来源版本／位置无法复现时显示具体缺口；可以打开当前资料但标为当前版，不静默替换历史依据。

首批只保证一次分支往返。Workspace 的一个 revision 不足以恢复当时所有成员正文版本；本批固定的是上述问题、视图和来源引用，不宣称实现完整历史工作区快照或多层嵌套撤销。

## 6. 选择导出：明确带走哪些版本

旧请求 `{selected_refs, formats}` 保留 v1 行为与兼容性。B 新界面建议使用另一种显式请求：

```json
{
  "object_selections": [{"id": "DEMO-object", "revision": 2}],
  "view_selections": [],
  "formats": ["json", "markdown"]
}
```

上例是假 ID 的合同示意，不是实际可执行请求。新旧选择方式不混用；同一次导出可显式选择同一对象的不同版本，界面分别标注。新输出标 `schema_version=2`，JSON 与 Markdown 表达一致：

- 正文只取 object_selections 的指定版本。工作区中未选择的成员仅列引用，不取其正文。
- 视图只取 view_selections，须同时选择它所属的 Workspace；选工作区不自动带出全部视图。继续点／草稿线也在导出预览中明示。
- 枚举本批的目标、知识、要求、尝试、前次尝试、问题、evidence_refs、branch_origin 及已有关系引用；external_refs 逐条写引用类别、ID、已知版本和来自哪个字段。同 ID 的 r3 已选，不等于引用的 r2 已包含。
- 来源只导出所选记录携带的 SourceRef，并显示“原文件／历史字节未包含”；不递归获取整个网络，不复制原文件或未选的个人产物。
- 缺少选定版本时明确失败、保留选择；不能导出最新版本冒充它。旧引用未固定 revision 时如实保留未知。

这是读取和选择语义的窄扩展，不含归档所有历史、导入恢复、同步服务或新的备份平台。

## 7. 对原 B 验收的具体化

| 原验收 | 增加的明确检查，不增加新包 |
|---|---|
| B-02／03 | 同一 K 在考研与鲁侧有不同要求；只改一份要求不改另一份或个人结果；某档未定义时不显示已覆盖 |
| B-04／05／07 | 强帮助成功与独立失败并存；反馈引用 T 的旧版、更正仍可追溯；研究判断与学习反馈分别修订 |
| B-06 | 两个 View 中原 View 不是最近更新者仍能返回；原内容后来更新时不被恢复动作覆盖；分支重开后原 Q 身份不变 |
| B-09 | 选择旧 r2 时确实带出 r2；只选判断不夹带 Attempt 正文；同 ID 的 r3 不消除 r2 的外部引用缺口；选 Workspace 不夹带其他 View |
| B-10 | 新 kind 的创建、条目写入、修改、查询和导出均可用；旧 Feedback／View／v1 导出仍按原约定读取 |

本轮只有代码静态核对和纸面设计，以上全部是未来验收预期，未运行、未计 PASS。

## 8. 可直接用于范围确认的结论

建议按 **A → B** 分段施工：先修来源检索和首次保存，再落实本件记录及往返接口。两批分别收回执，不因 A 完成自动关闭 C03 用户复验；B 的字段及使用反馈仍按首批方案 G2／G3 处理。

本次已把 B 的关键接口选择列出，未决点不再泛指“以后再定模型”。现在需要确认的是是否采用上述窄约定并批准施工范围，而不是再扩一轮系统架构。正式实施时将获批选择及实际差异记入实施任务的 CONTRACT_DELTA，本稿保留为设计来源。
