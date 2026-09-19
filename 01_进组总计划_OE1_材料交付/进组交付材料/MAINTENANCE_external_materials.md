# 对外材料套件 · 维护手册(MAINTENANCE_external_materials)

> **给谁看**:后续维护窗口的 Agent 与用户本人(改口径、过时点、跑复查时)。
> **配套**:交接总档案 `progress/handoff/2026-08-13__w-external-materials-handoff.md` ｜ 使用手册 `GUIDE_external_materials.md` ｜ 口径单一事实源 `factcheck_onepager_20260813.md`。
> 2026-08-13 建。维护原则:**先改依据(factcheck),再改正文(8 文本单元),后重渲染,最后登 CHANGELOG**——四步缺一不可。

---

## 一、口径登记册(当前生效口径,改动须走 §三流程)

| # | 口径项 | 当前生效值 | 依据 |
|---|---|---|---|
| 1 | 论文名称 | **ProbGuard** 为主名;每个可独立外发文本单元首现括注"(原名 Pro2Guard,ASE 2026)/(formerly Pro2Guard; ASE 2026)",第二次起直写;代码仓库仍名 Pro2Guard | factcheck §1.1(2026-08-13 arXiv 实时页核验) |
| 2 | 评测域表述 | "具身、自动驾驶与 web / embodied, autonomous-driving, and web" | factcheck B5/C1(ProbGuard 摘要含自动驾驶) |
| 3 | 域空白句 | 必须同时带:时点限定("在我 2026 年 8 月的调研中/as of my August 2026 survey")+ 收窄限定("带概率保证的同类护盾工作/probabilistic-shielding work") | factcheck C2;SEARCH_BOUNDARY 有界口径;SIIHA 边缘先例 |
| 4 | 保证边界句 | "不声称端到端形式保证(保证止于符号模型层)/no end-to-end formal guarantee is claimed" 每版必含 | INDEX §4 + T5 禁语节 |
| 5 | 数字锚定值 | 约 8,800 行(精确 8,824 只进 factcheck)/43 单元测试/2,400 条/Qwen2.5-7B+q4_k_m(约 4.7 GB,仅 C 版正文)/数月/数千轮/4,470 行/23 核/自适应 Metropolis-Hastings(严禁 HMC/NUTS/Truthometer) | factcheck §D 实测;v3 邮件包装词纪律表 |
| 6 | XES/GraphML 双出口 | 只可表述为互操作事实("经 PM4Py/networkx 读取验证"),严禁实验/研究结果口径 | 039 波审计 Gate R0 FAIL |
| 7 | 身份 | 本科生(2026-09 大三)/undergraduate;考研 2027-12、读研 2028 起对外不提 | v1 撰写说明第 2 条(身份勘误) |
| 8 | 复现计划 | **ReGA 先行复现;ProbGuard 定向精读**(对外措辞"官方仓库现处重构中,改以论文与代码对照的定向精读跟进") | 用户口头 2026-08-13 22:21;v1 撰写说明第 10 条存证 |
| 9 | 谓词表 | v0 **已完成**(INTIMA 31 类 → 16 个带时间窗可执行谓词),完成时态;双人标注/κ/trace 导出/最小闭环仍为计划,**严禁说满** | 同上 |
| 10 | 脱敏 | 自有系统只称"自建长期人机交互平台";涉数据一律"经脱敏的(纵向)交互日志" | proposal-notes 统一脱敏原则 |
| 11 | 鲁场景纪律 | 不提孙猛/PKU/考研;零 shield/护盾/DTMC/iMDP/PAC/概率保证词;姿态=请教+踏实跟学 | OE1 v4 §3;onepager_lu_variant 任务一 |

## 二、时点维护台账(按日期触发)

| 时点 | 动作 | 出处 |
|---|---|---|
| **8-25 起(BR-1,死线)** | 复查 NSFC 放榜(山科大官网喜报→NSFC 官网→LetPub 交叉),定 OE1 分支 A/B;8-31 仍查不到按 A 分支不等 | `OE1_send_kit.md` SOP |
| 9-1~15 | OE1 投递窗(推荐 9-7/9-8 上午;避开学第一周与教师节 9-10) | 同上 |
| 9 月底 | OE1 无回复则跟进一次;备选:本校老师引荐 | 同上 |
| **2026-10-12~16(ASE 2026 会期)后** | 名称括注可简化:会后学界普遍知晓 ProbGuard,新起草材料可省"(原名 Pro2Guard)"括注(已发材料不追改);顺带执行 factcheck L2(ASE accepted list 复核) | factcheck §1.1 理由① |
| 每月雷达日 | ①arXiv:2508.00500 页复查(副标题两说,L1);②"长期交互域护栏"竞品扫描(SIIHA 类,防空白句失效);③ShieldAgent/ReGA 归属与版次复查 | factcheck L1/L5;FOCUS 重心 4 月度雷达 |
| 用户定稿时 | 教育年份确认(2024.09–2028.06 系推算);量化数字放行逐项确认 | resume 尾注;final_review §⑤ |

## 三、口径变更流程(任何一条口径要改时)

1. **改依据**:在 `factcheck_onepager_20260813.md` 追加增量条目(日期+证据 URL+新裁定;原条目不删,标"已被 X 取代")。
2. **改正文(8 文本单元清单)**:`onepager_draft_v1.md` 中文版+英文版;`onepager_v2_voices.md` A/B/C;`onepager_v2_voices_en.md` A/B/C。视口径涉及面加改:`onepager_lu_variant.md` 鲁版正文、`resume_onepage.md` 中英、`diagram/*.mmd`(图内文字)。**改完跑 §四机械验证**。
3. **重渲染**:`cd render/ && ./render_onepager.sh ../onepager_draft_v1.md --zh && ./render_onepager.sh ../onepager_draft_v1.md --en`(定稿单文件同理)。
4. **登 CHANGELOG**:`map/CHANGELOG.md` 增量行(动 map 必登,四铁律)。

## 四、机械验证命令集(改动后必跑,全部在 proposals/ 目录下)

```bash
# 1) 裸旧名残留(应零输出;括注/记录档豁免)
rg -n "Pro2Guard" onepager_draft_v1.md onepager_v2_voices.md onepager_v2_voices_en.md resume_onepage.md \
  | rg -v "原名|formerly|原 Pro2Guard|仓库仍名|repo"

# 2) 禁语扫描(对外正文应零输出)
#    豁免说明:v1 撰写说明第 4/5 条、lu_variant 任务一与附录自查表、各文件头部说明区
#    本身含禁词字样(自查记录性质),故只扫正文区切片,不整文件扫。
rg -n "全球唯一|无人区|保证所有|无漏报|证明.{0,6}安全|the only|guarantee.{0,12}all|no false negative" \
  onepager_v2_voices.md onepager_v2_voices_en.md resume_onepage.md diagram/*.mmd
awk '/^## 中文版/,0' onepager_draft_v1.md | rg -n "全球唯一|无人区|保证所有|无漏报|证明.{0,6}安全|the only|guarantee.{0,12}all|no false negative"
awk '/^## 任务二/,/^## 任务三/' onepager_lu_variant.md | rg -n "全球唯一|无人区|保证所有|无漏报|证明.{0,6}安全"

# 3) 脱敏与人名(正文区应零输出;lu_variant 只扫任务二正文节,任务一/三与附录属内部分析豁免)
rg -n "人机恋|AI 伴侣|角色扮演|张重熙|romantic|role-play|Jun Sun|Meng Sun" \
  onepager_v2_voices.md onepager_v2_voices_en.md resume_onepage.md
awk '/^## 任务二/,/^## 任务三/' onepager_lu_variant.md | rg -n "人机恋|AI 伴侣|角色扮演|张重熙|孙猛|PKU|北大|考研"

# 4) 空白句双限定齐全(voices 与 voices_en 各应 =3,即三个声音版全带)
rg -c "2026 年 8 月的调研|August 2026 survey" onepager_v2_voices.md onepager_v2_voices_en.md
rg -c "带概率保证的同类护盾|probabilistic-shielding" onepager_v2_voices.md onepager_v2_voices_en.md

# 5) 鲁版正文零术语(应零输出;切片终点=「## 任务三」,勿写成「## 三」否则吞进附录自查表误报)
awk '/^## 任务二/,/^## 任务三/' onepager_lu_variant.md | rg -n "shield|护盾|DTMC|iMDP|PAC|概率保证|LLM|大模型"

# 6) 占位符残留与脚本自测(语法+试跑见脚本头注释)
bash -n fill_placeholders.sh && rg -o "\[[^\]]{1,20}\]" onepager_v2_voices*.md resume_onepage.md | sort -u
```

## 五、遗留项台账(转录自 factcheck L1-L7 + 终审,处置后在此打勾)

- [ ] **L1** ProbGuard 副标题两说(arXiv 现页 "Proactive Runtime Monitoring…via Probabilistic Prediction" vs 索引源另说)——引用全称前点开 arXiv 页确认;一页纸只用系统名,不受影响
- [ ] **L2** ASE 2026 官方 accepted list 复核(现依据=arXiv camera-ready 会议头,强证据;会前复核一次绝对稳妥)
- [ ] **L3** MIT/OpenAI RCT 正式 venue 未见——口头称"arXiv 预印本"最稳
- [ ] **L4** INTIMA 会议归属未标注——维持只写 arXiv 号
- [ ] **L5** proposal-notes 其余文献(Badings/dtControl/Position/DiverseGuide/NeMo/RvLLM/Agent-C/Ctrl-G/OCC/Verified Detection/CoAgent/SagaLLM/CRDT)未逐条网核——口头引用前按 factcheck 方法点验
- [ ] **L6** SIIHA 登 radar watchlist(watchlist 辖区窗口执行)
- [ ] **L7** 平台"数月/数千轮"实数未复核(量级口径风险低;要精确数需用户授权另测)
- [ ] **W4**(终审)声音文件不满足渲染切片约定——定稿时把选中声音摘成 v1 同构单文件再渲(GUIDE §二第 6 步已写操作法)
- [ ] **跨窗同步**:上游 `proposal-notes.md`(companion-survey 域)与 `T5_companion_prob_shield.md`/`INDEX.md` 的"12–16 谓词、Pro2Guard 复现"旧口径待各辖区窗口同步;FOCUS W-复现行"ProbGuard+AgentSpec 复现"口径待用户确认是否调整(FOCUS 系重心总纲,仅用户可改)

## 六、质检再跑法(需要重新终审时)

- 轻量:跑 §四命令集 + 人工过 `final_review_20260813.md` §② R1-R8 表逐项自查。
- 完整:新起终审 Agent,prompt 以 final_review 头部"审查对象/审查项 R1-R8/只报告不改稿"为模板,基准文件=factcheck(含增量)+ INDEX §4 + OE1 §3;产出命名 `final_review_YYYYMMDD.md`,不覆盖旧报告(审计链只追加)。
