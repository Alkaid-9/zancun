# ra28 专属窗口协议（KICKOFF）

**本窗职责**：只管 `ra28-mindbridge` 训练包的完整生命周期（赛前准备 → 做题 → 批改 → 复盘）。不碰其他训练包、不动 progress 权威链（除批改后按 BRIEF §4 转正的产出）。

## 阶段 1 · 赛前准备（本窗第一动作，用户不在场也能跑）

> **幂等检查（先做）**：若 `_sealed/EX-01_answer.md` 已存在且带 completion footer、且 mindbridge 已有 git 与 venv——赛前准备已由协调窗代理完成（8-12 晚并行发动），本阶段全部跳过，直接报"就绪"等用户进场做题。部分完成则只补缺项。

1. 读 `BRIEF.md` 全文 + `../00_SYSTEM.md` §2/§3/§7。
2. **环境前置（主控 shell 直接做）**：
   - `D:\Workspace\mindbridge` git init + `.gitignore`（排除 `mindbridge-qwen2.5-7b-ft-q4_k_m.gguf/` 与 `psychqa_synthetic.jsonl/` 两个数据目录）+ 首 commit（快照基线）。
   - `mindbridge-py` 建独立 venv 装 `requirements.txt`（13 个依赖，含 chromadb 稍重，后台跑）。
   - 冒烟：`scripts/run-dev.sh` 或直接 uvicorn 起服务——**起不起得来都记录现象**（MySQL/Redis 缺失属预期，这是 EX-02 的真实素材，不修）。
3. **派 Setter（必须子代理后台，绝不在本窗对话里分析代码——分析过程可见即剧透）**：
   - Setter-1（现在派）：按 BRIEF §2 EX-01 范围独立盲 review → `_sealed/EX-01_answer.md`。
   - Setter-2（EX-01 做完后、EX-02 开始前派）：独立 verdict 基线 → `_sealed/EX-02_answer.md`。
   - Setter-3（EX-02 后派）：`training/ex03` 分支埋 3 雷 + 症状报告（症状放 `EX-03/`，根因进 `_sealed/`）。
   - **Setter 回执格式（硬规则）**：只报「完成 + 产物路径 + 条目数」，禁止出现任何具体发现/雷位/结论。
4. 就绪后报给用户一行：环境状态 + Setter-1 密封条目数 + "可开始 EX-01"。

## 阶段 2 · 做题（用户发话"开始 EX-NN"触发）

- 主控计时（90 分钟），提醒用户禁读清单（BRIEF §0 第 4 条 + `_sealed/`）。
- 主控当 Coach：只响应"卡死"请求，按 H1→H2→H3 逐级，禁止跳级；记录解锁级别。
- 时间到提醒提交；未完成也提交。

## 阶段 3 · 批改与复盘

- 用户交付后主控才可开封 `_sealed/`（此前主控也不读）。按 BRIEF rubric 出批改单（召回/误报/过程分 + 3 条最有价值差距）。EX-04 走苏格拉底三轮。
- 陪用户复盘 → 触发铸卡的（EX-01/02/03）把方法论卡写进 `../methodology/` 并登记 INDEX。
- **LEDGER 追加约定（多窗口单写者）**：只在 `../LEDGER.md` 末尾追加本包的行，绝不改动其他行。
- EX-05 完成后：三场景 log 复制一份到 `MAS_Safety_Project/research/pm4py_toy/data/`（ra26 窗口要用），并在回执里注明。

## 断点恢复

新会话进来：读本档 + `../LEDGER.md` 查 ra28 最后一行 → 接着对应阶段走。
