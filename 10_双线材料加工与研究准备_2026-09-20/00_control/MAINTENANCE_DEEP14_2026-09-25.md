# Deep14 存档维护与故障处置手册

**运维对象仅为 zancun 文档/任务/证据索引；非 LearnGraph 服务器、用户账号或原 MAS 仓。** 当前用户已暂停论文生产；本手册中的“恢复后”步骤一律以新的明确指令为前提。档案日期 2026-09-25 PDT（UTC 09-26）。

## 1. 权威、路径与写权限

- 入口：包内 `00_START_HERE.md` → `00_control/HANDOFF_DEEP14_WINDOW_2026-09-25.md`；执行状态：`00_control/TASKS.tsv`；输入池：`00_control/PAPER_POOL.tsv`、`资料输入清单.tsv` 与 `R2_C0_2026-09-25.md`；论文接收范围：各篇 `B/papers/<slug>/ACCEPTANCE.md`。若概述与任务表冲突，先保存两边文本/时间再调查，**不要偷偷把概述当执行权威**。
- 本窗口写域：上述包内 `00_control/` 的本窗口新档案、精确的 `TASKS.tsv` 行、本窗口 CA 包与 `00_START_HERE.md` 的暂停指针。进入时已有的 `.claude/gemini-guard/test_guard.py`、`worker.py`、`.claude/gemini-guard/README.md`、`GEMINI_WORKER_CONTRACT.md`、`DRAFT_00_OBJECTIVES_AND_CLAIMS.md`、`DRAFT_04_BRIDGE_LU_SUN_OPENAI.md` 属其它工作；不能清理、纳入本窗口成果或替它们签收。
- 原研究仓 `/mnt/d/MyResearch/MAS_Safety_Project` 只读；受保护题、作答、sealed/holdout 不读不写；服务器/部署/账户/配置/外联不属本维护范围。未经另批不 stage/commit/push/批量改源稿。任何新窗口接管前记录其自己的 HEAD/dirty 基线。

## 2. 只读巡检与归档校验（在仓库根运行）

```sh
git branch --show-current
git rev-parse HEAD
git status --short
python3 - <<'PY'
import csv, hashlib, pathlib
r=pathlib.Path.cwd()
m=r/'10_双线材料加工与研究准备_2026-09-20/00_control/WINDOW_ARCHIVE_MANIFEST_2026-09-25.tsv'
with m.open(encoding='utf-8', newline='') as f:
    rows=list(csv.DictReader(f, delimiter='\t'))
bad=[]
for x in rows:
    p=r/x['path_from_repo_root']
    if x['sha256']=='SELF_EXCLUDED':
        continue
    if not p.is_file(): bad.append((str(p), 'MISSING')); continue
    raw=p.read_bytes()
    if len(raw)!=int(x['bytes']) or hashlib.sha256(raw).hexdigest()!=x['sha256']:
        bad.append((str(p), 'DRIFT'))
print('rows=',len(rows),'hash_checked=',sum(x['sha256']!='SELF_EXCLUDED' for x in rows),'errors=',bad)
if bad: raise SystemExit(1)
PY
```

验收仅表示档案清单所列字节未变；不证明 PDF 主张正确、manifest 外的文件不存在，或来自用户的学习证据已验收。清单**不自哈希**，自身行 `SELF_EXCLUDED`，可以用 Git diff / 独立存储的哈希核清单；若已有经批准的更新，先留旧清单，再生成带日期/版本的新清单，不篡改历史记录。源 PDF 另比 `R2_C0...` 与 `DEEP14_WAVE1_DISPATCH...` 的 SHA；此归档清单不拷贝/打包原 PDF。

## 3. 对账与变更规范

1. 若论文 PDF/旧稿变动：停受影响论文；记录**旧/新路径、SHA、日期、标题版本、哪些 claim 引用它**；独立重核相关页后才能出新验收；旧回执注明被覆盖/过期，不悄悄改旧哈希。跨源主张逐条标 PDF 物理页＋章节/编号；关键数学符号渲染核对。
2. 若已有包发生修改：核独立日志与 manifest hash，读当前文件，不覆盖另一窗口产物；先新增差分和新验收 ID，再更新精确任务行。`TASKS.tsv` 只在落盘真实证据后升级，主张状态、运行状态、独立复核状态、本人学习状态四轴独立记；无证据则 `UNKNOWN/PARTIAL/NOT_RUN`。
3. 若要执行计算（**需另获授权**）：先冻结 fixture＋独立期望＋脚本/依赖版本，在隔离工作目录生成不可覆盖的 `run_id`，保存真实命令、cwd、起止时刻、env、代码/输入 SHA、真实 exit、原始 stdout/stderr、断言和误差；失败也保留。无计算价值的理论分析可独立手推，但需说明“未运行”与推导的覆盖范围。若未实现 `tools/capture.py`，禁止编造它的回执。
4. 每次更新后检查 `README → sources/claims → analysis/fixtures → ACCEPTANCE → TASKS → HANDOFF` 能双向定位，清单只覆盖**已存在**的本窗口文件；追加操作日志的时间必须是实际观测，没记录的写 `TIME_NOT_CAPTURED`，不回填推算时间。归档 manifest 应在**所有正文编辑完成以后**重建；避免指向将来才会创建的产物却写“已存在”。

## 4. 故障表、止损与回滚

| 情形 | 即刻动作 | 可恢复条件 |
|---|---|---|
| Agent 三连 transport error 或新短包再断 | 保留错误原文/任务规格，接受研究内容数记 0；不估 token，不续投全文 | 用户明确恢复后可用一节窄包核路由；再失败转控制器逐篇回源，不诊断臆测原因 |
| PDF 页码/公式与文本抽取冲突 | 把相关 claim 降为 `UNKNOWN`，渲染原页对照、记图像页号 | 有逐符号复核与独立挑战后才能回升级 |
| 反例对象/金标由同一算法生成 | 反例设 `SPEC_ONLY/NOT_RUN`，停止引用为证据 | 独立 oracle 或预冻结手算和真实运行记录 |
| 共享文件/背景 dirty 被其他窗口改动 | 仅停冲突路径，保留现状和双方 SHA；不全仓 `reset/clean` | 明确归属和差分后新文件/精确行修订 |
| A 学习答案泄漏、错将 AI 材料写 USER PASS | 停教学释放，保持 EX-06 LOCKED，隔离相应材料 | 依据原课程权限与本人真实回执单独审查，不由 B 线背书 |
| hash 巡检失败或入口断链 | 保留原 manifest 与当前文件；记录 MISSING/DRIFT 的精确路径和修复责任 | 对照 Git/原始快照定位后另建新版本清单，不能修改旧收据装作未变 |

归档回滚只允许**逐文件**识别本窗口新增路径；保留用户和其它窗口全部六项背景差异。回滚只是撤去错误主张/错误入口，不等于删原件或推翻其他已验收材料。旧状态有疑问时保守标 `PARTIAL` 并写证据缺口，避免虚假“14/14 已做”。
