# D1 材料复核回执

状态：`PASS-WITH-USER-ACTION-OPEN / BLOCKERS=0 / NO-USER-PASS`

## 范围

复核 A0–A5、控制基线、14 篇论文池和 reviewer-only 隔离运行的来源链。复核者只读，未运行学习者脚本，未读 sealed/holdout/answer/reference/retest 正文。

## 首轮发现与修复

| 严重度 | 发现 | 修复 | 复核状态 |
|---|---|---|---|
| BLOCKER | A5 直接披露预检 exit code 和 10 行正式题数字 | 从 A 入口移除结果、日志直达和存放路径；运行证据标 reviewer-only | CLOSED |
| BLOCKER | 入口不能直达题面、三个 WIP 和 EX-06 门禁 | `START_HERE.md` 增加 7 个公开直达链接；TSV 改为绝对路径 | CLOSED |
| HIGH | 首次 run 缺时间、执行副本哈希和真正空 stderr | 新建 provenance 完整的 reviewer-only run，保留首次 run 为不完整历史 | CLOSED |
| MEDIUM | 控制表相对路径基准混用 | `INPUTS.tsv`、`PAPER_POOL.tsv`、`CURRENT_STATE.tsv` 统一为绝对路径 | CLOSED |
| MEDIUM | invariant 微例与公开题面三张卡过于同构，Git diff 无微例 | 换为几何平移微例；增加临时文本 diff 练习 | CLOSED |

## 二轮冷启动

- 阻断项：`0`
- 首次打开入口到定位 R1/EX-05/EX-06 七个公开对象：`12 秒`
- 完成链接、路径、JIT 和 run metadata 的全部定点复核：`163 秒`
- `START_HERE.md` 中 13 个 Markdown 链接全部存在；7 个学习直达对象均不在 `_sealed`。
- `CURRENT_STATE.tsv` 14 个证据行路径均可唯一解析，行号在文件范围内。
- JIT 8 节均有与正式题不同的微练习。
- reviewer-only run 有 command、cwd、start/end、执行副本哈希、exit、stdout/stderr 哈希和输入前后哈希；复核者未读 raw stdout/stderr 内容。

## 当前状态上限

- 材料：`READY`
- AI 隔离运行：`REVIEWER-VERIFIED-PROVENANCE`，结果对学习者暂不释放
- 本人运行：`NOT-STARTED`
- R1 提交：`MISSING / USER-ACTION-OPEN`
- EX-05：`WIP / PASS-NOT-DECIDED`
- EX-06：`LOCKED`
- 本人能力：`NOT-ASSESSED`

A6 和 A7 必须消费 D1 真实回执；在回执出现前不预造 D2 分支。
