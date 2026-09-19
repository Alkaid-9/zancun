# 对外材料套件 · 使用手册(GUIDE_external_materials)

> **给谁看**:用户本人(定稿、外发时);接手定稿装配的新窗口 Agent。
> **配套**:交接总档案 `progress/handoff/2026-08-13__w-external-materials-handoff.md`(总览)｜维护手册 `MAINTENANCE_external_materials.md`(口径与时点)｜放行检查单 `final_review_20260813.md` §⑤(权威,外发前必过)。
> 2026-08-13 建。所有正文仍是**草稿,未经用户确认严禁外发**。

---

## 一、这套材料是什么(30 秒)

9 月进组的对外自我介绍套件:**一页纸 Research Statement(主件)+ 一页简历(配套)+ 管线示意图(面谈用)+ OE1 邮件发信包(鲁法明线)**。
一页纸有 4 个候选:v1 混合声(基线)、声音 A(谦逊)、声音 B(研究者)、声音 C(工程),中英成对;另有**鲁版**(受众=鲁法明,Petri 网/流程挖掘叙事,与通用版不可混用)。
所有版本**事实与数字完全一致**,只差语气与组织——挑任何一版都不用重新核对事实。

## 二、快速定稿(10 分钟流,按顺序)

1. **挑声音**:打开 `onepager_v2_voices.md`,读 §一对比导读表(4 行)与 §二推荐意见,在 §六勾选 A/B/C 或维持 v1。英文自动取 `onepager_v2_voices_en.md` **同字母**版本。
   - 拿不准就选 **A(谦逊)**:与 OE1 邮件姿态同源,初次见面最稳;B 留组会汇报,C 留展示执行力场合。
2. **填占位符**:打开 `placeholder_sheet.md` → §二给 **[课题组] 口径一句话**(9 月进组对象与鲁法明邮件是否同一件事)→ §三把 config 模板抄成本目录 `placeholder_config.env`,填约 10 项(表里标了候选值与状态)。
3. **跑替换**:
   ```bash
   cd /mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals
   ./fill_placeholders.sh onepager_v2_voices.md onepager_v2_voices_en.md resume_onepage.md
   ```
   看输出末尾"残留扫描"=无未替换占位符即通过(选填项留空的,发稿中把该字段整句删掉)。产物是 `*_filled.md` 副本,原稿不动。
4. **量化数字放行**:确认愿意公开——约 8,800 行 / 43 单元测试 / 2,400 条 / 约 4.7 GB(仅 C 版)/ 4,470 行 / 23 核(简历)。不愿公开哪个就在发稿副本里删哪个。
5. **摘正文外发**:从 `_filled` 副本中把**选中声音的正文节**(`# Research Statement · 姓名` 起四段)单独摘出,删掉所有中文说明区(头部红线、导读表、§六、尾注)。
6. **渲染 PDF**(需要打印版才做):把摘出的正文存成单文件(结构照 `onepager_draft_v1.md`:`## 中文版` 区头 + `#` 一级标题 + 正文;英文区头 `## English Version`),然后:
   ```bash
   cd render/ && ./render_onepager.sh ../你的定稿.md --zh   # 或 --en
   ```
   Windows 里打开 `render/out/*.html` → Ctrl+P → 另存为 PDF(**边距选"无"**,取消页眉页脚,详见 `render/README.md`)。

## 三、分场景用法

| 场景 | 用什么 | 注意 |
|---|---|---|
| 进组自我介绍(通用) | 选中声音的一页纸 + 简历,成对递交 | 简历回答"做过什么",一页纸回答"要研究什么/为什么是我" |
| **任何鲁法明触点** | **只用 `onepager_lu_variant.md` 鲁版正文** + 按简历尾注"递鲁场景"微调简历 | 严禁用通用版(概率护盾叙事对鲁全轴错位,分析见该文件任务一);图只用 `pipeline_lu`,导出改中性文件名 |
| OE1 首封邮件(9 月) | 按 `OE1_send_kit.md` 走(8-25 BR-1 → 定分支 → 9-7/9-8 发) | **首封不附一页纸**(轻附件方案:PM4Py notebook + demo 截图);一页纸留第二触点 |
| 面谈展示 | `diagram/` 两图(mermaid.live 粘贴导出 SVG/PNG) | 通用场景用 `pipeline_shield`,鲁场景用 `pipeline_lu`;导出文件名中性化(如 `method_pipeline.svg`) |
| 考研复试等后续场合 | v1/声音版按受众微调 | 参照 `onepager_lu_variant.md` 任务三的场合分工逻辑 |

## 四、红线速查(外发前 60 秒自查)

1. **脱敏**:自有系统只叫"自建长期人机交互平台 / self-built long-term human-AI interaction platform";全文零"人机恋/AI 伴侣/角色扮演"。
2. **名称口径**:ProbGuard 为主名,首次出现括注"(原名 Pro2Guard,ASE 2026)";口头可补"代码仓库仍挂旧名"。
3. **空白句**:必须同时带时点("在我 2026 年 8 月的调研中")与收窄("带概率保证的同类护盾工作");口头也别说宽(SIIHA 类规则式先例存在)。
4. **身份**:本科生(2026-09 大三)/ undergraduate,永不写研究生。
5. **人名**:正文零作者人名;口头引用注意 ProbGuard/AgentSpec 出自 SMU **Jun Sun** 组,与 PKU **Meng Sun** 是两个人。
6. **XES/GraphML 双出口**:只说"经 PM4Py/networkx 读取验证"(互操作事实),不说实验/研究结果。
7. **既成事实边界**:谓词表 v0(16 个)可说已完成;双人标注/κ/trace 导出/DTMC 闭环仍是计划,别说满。
8. 说明区(所有中文注释节)外发前必须删干净。

## 五、文件索引

| 文件 | 一句话 |
|---|---|
| `onepager_draft_v1.md` | 混合声基线(含撰写说明=全部纪律的原始出处) |
| `onepager_v2_voices.md` / `_en.md` | 三声音候选中/英,§六拍板处 |
| `onepager_lu_variant.md` | 鲁版正文+冲突分析+场合分工 |
| `resume_onepage.md` | 配套简历中英 |
| `factcheck_onepager_20260813.md` | 事实核查(口径单一事实源;遗留项 L1-L7) |
| `final_review_20260813.md` | 终审报告;**§⑤=放行检查单(权威)** |
| `placeholder_sheet.md` / `fill_placeholders.sh` | 占位符主表 / 一键替换 |
| `OE1_send_kit.md` | OE1 发信时间线+SOP+checklist |
| `render/` | md→A4 HTML 渲染管线(README 含打印步骤) |
| `diagram/` | 两张 mermaid 管线图+出图法 |
