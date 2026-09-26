# Deep14 交接包使用手册（读者/下一窗口）

**本手册只教阅读、判断与恢复上下文；不是论文生产命令。当前 `D14-SCOPE=PAUSED_BY_USER`。** 本地档案日 2026-09-25 PDT，UTC 日期 09-26；旧 D1/D2=09-22/23 是过期历史计划。仓库根：`/mnt/d/Alkaid/Desktop/zancun`（Windows `D:\Alkaid\Desktop\zancun`），目录：`10_双线材料加工与研究准备_2026-09-20/`。

## 最短读法（约 5 分钟定位，不承诺 5 分钟理解论文）

1. 打开 `00_control/HANDOFF_DEEP14_WINDOW_2026-09-25.md` 看窗口时间、完成/未完成、Git 背景差异；再看 `00_control/WORK_LOG_DEEP14_2026-09-25.tsv` 的每条可追踪操作。`00_control/TASKS.tsv` 是执行状态权威，筛 `D14-`、`R2_INCREMENT`、`TB0`；`03_两天任务看板.tsv` 不是当前执行状态。
2. 找一篇：`00_control/PAPER_POOL.tsv` 查原 11/增量 3 身份；原 11 PDF/旧稿路径在 `资料输入清单.tsv`（相对**仓库根**）；新增三份 PDF/哈希在 `00_control/R2_C0_2026-09-25.md`。纸面队列不代表相应的 `B/papers/<slug>/` 已建成。
3. 唯一新包 `B/papers/contragent/` 的阅读顺序：`README.md` → `sources.tsv` → `claims.tsv`（按 ID）→ `analysis.md` → `DELTA.md` → `reuse.md` → `fixtures/predicate_blindspot_pairs.json` → **最后重读 `ACCEPTANCE.md` 的 OPEN 门**。其中 PDF 原件是 `CA-PDF`、旧稿是 `CA-OLD`；不可反过来用旧稿覆盖原文。36 行是候选来源定位，不是 36 项均经独立验证。两对 fixture 是 **NOT_RUN** 规格。
4. 想查“为什么没有 PNULock/SBPN 包”：`00_control/DEEP14_WAVE1_DISPATCH_2026-09-25.md` 有 3 个任务的输入哈希/返回错误/接受数 0；`DISPATCH_SPECS_2026-09-25.md` 存预期问题，不是收到的研究结果。当前状态看 `TASKS.tsv:D14-PNU/D14-SBPN/D14-CA`，不要把派工规格当产物。
5. 想看完整方向/权限：`ARCHITECTURE_DEEP14_2026-09-25.md` 是当下架构快照；`NEXT_PLAN_DEEP14_2026-09-25.md` **只是恢复后提案**。本次档案的物理完整性看 `WINDOW_ARCHIVE_MANIFEST_2026-09-25.tsv`，它不是论文内容审核结论。

## 如何理解状态，不越线消费

| 看见字段 | 含义 | 不意味着 |
|---|---|---|
| `MATERIAL_READY_USER_ACTION_OPEN`（A线） | 历史 AI 材料与冷启动复核已就绪，等用户本人 R1/EX-05 | 本人已学习、EX-05 PASS、EX-06 解锁 |
| `QUEUED`、`PDF_HASH_VERIFIED` | 论文身份/输入或排队检查 | 已读全文、旧稿全真、深拆完成 |
| `PARTIAL_SOURCE_REVIEW`（仅 CA） | 主控从本地原 PDF 覆盖 13 页并落下部分来源审阅 | 异构 Agent 审核、可运行反例、作者实验复现、研究方向确立 |
| `TRANSPORT_ERROR`（三 Agent） | 此路由没有可用论文报告；原因与花费未知 | 论文已拆，或可断言是模型服务端、文件大小造成 |
| `NOT_RUN`、`PEER_REVIEW_OPEN` | 尚无对应命令/独立复核证据 | 可以因文件存在就写 PASS |

如果只要当前进度：**14 篇排队、1 篇 CA 部分来源包、0 篇全文深拆验收**；A线本人学习证据未变，`B/PAPER_QUEUE.tsv` 未建。要讨论交叉比较/教学/研究，请限定到已被 `ACCEPTANCE.md` 接纳的 claim 范围；不可从 CA 规格推出服务器已验证或用户能力已提升。

## 下一窗口安全操作

先按维护手册校验 Git 状态、档案 hash、来源输入身份与指针；**仅当用户再次明确恢复后**按下一计划确定一篇和一个狭窄关口。需要真实运行时另核独立预期、执行权限和输出隔离；不得把示例 `tools/capture.py` / `tools/run_checks.py` 命令直接复制运行，规划里提过但本窗口未建。用户如只要问现状、修交接或改变计划，保持只读/文档侧，不触发论文 Agent。需要学习请另看 `A/D1/START_HERE.md`，不要从本交接生成本人答案。
