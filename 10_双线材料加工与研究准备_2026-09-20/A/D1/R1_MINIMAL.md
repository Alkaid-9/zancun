# A1 R1 最小提交框架

状态：`BLANK-FRAME / USER-MUST-WRITE / 30-MINUTE-CAP`

## 先找，不先重写

先查你的仓外笔记。如已有 G0 五问稿，只记路径并停止重写：

```text
我的既有稿路径：
是否包含五问：
来源标签是否齐全：
第 3 问是否已标 exposure：
```

指定提交路径：

`/mnt/d/MyResearch/MAS_Safety_Project/research/tracebridge_full_spectrum_20260830/00_control/_scratch/seg0/G0_user_paper_note.md`

本文件只是空框，AI 不会写入上述指定路径。

## 顶部：原有读前预测

```text
PREDICTION p1：
核对后：✓ / ✗ / 没答案
依据：

PREDICTION p2：
核对后：✓ / ✗ / 没答案
依据：

PREDICTION p3：
核对后：✓ / ✗ / 没答案
依据：
```

## 五问

每条陈述都使用 `PAPER-TEXT / USER-INFERENCE / AGENT-SUMMARY / UNKNOWN` 之一；`PAPER-TEXT` 必须带 PDF 页码和原句定位。

### 1. Algorithm 1 的合同

```text
输入：
维护的状态：
保留判据：
终止条件：
输出：
来源标签与页码：
```

### 2. 预算与保留量

```text
有无预算参数：
保留量由什么决定：
来源标签与页码：
```

### 3. 过滤后 DFG 边频次的来源

```text
EXPOSURE: Sol hint; 本问只算回 PDF 核实，不算独立发现。
我在 PDF 中找到的原句：
PDF 页/印刷页：
我核实后的表述：
来源标签：PAPER-TEXT / UNKNOWN
```

### 4. Stage 1 全局 R 与 Stage 2 局部 Ri

```text
两者各自是什么：
是否带权：
找不到的部分：UNKNOWN
来源标签与页码：
```

### 5. 逐句来源检查

```text
我有哪些 PAPER-TEXT：
我有哪些 USER-INFERENCE：
我见过哪些 AGENT-SUMMARY/提示：
哪些仍是 UNKNOWN：
```

## 到点断点

30 分钟到点即保存，不为补档吞掉 EX-05：

```text
已写到：
尚缺：
下次打开后的第一个动作：
```
