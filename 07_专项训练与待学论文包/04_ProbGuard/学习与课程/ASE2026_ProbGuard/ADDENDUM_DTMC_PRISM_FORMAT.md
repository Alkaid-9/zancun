# Addendum:DTMC 构造→PRISM 导出——数据格式与接口笔记(T5 谓词表对接件)

**日期**:2026-08-14(轻窗·定向精读,**只读未运行**;HEAD 半成品跑不通的 12 坑见 teardown,故本窗不做任何执行验证,冒烟命令仅列于 §7 供 W-复现窗)
**对象**:`/mnt/d/MyResearch/external/Pro2Guard`(commit `ab2f4ab`)`src/safereach/` 核心四文件 **`abstraction.py` / `predicate.py` / `build_model.py` / `runtime_monitor.py`**(+ `ctl.py`、`embodied/{build,abstraction,eval}.py`、`autonomous_vehicle/{abstraction,av_monitor}.py` 佐证格式)
**上游**:`research/map/oss_landscape/teardowns/ProbGuard_AgentSpec.md`(架构/数据流/12 坑,下称 **teardown**)+ 本目录 `03_PAPER_READ.md`/`04_DERIVATION.md`(方法语义)
**用途**:只回答一个问题——**T5 谓词表 v0(16 个带时间窗谓词)要接进"trace→DTMC→PRISM"管线,双方的数据格式、接口契约、属性文法各是什么**。所有断言均对照源码行号或仓内现成产物核实;推断处标注〔反推〕。

---

## ⓪ 三个版本层告警(照抄任何样例前必读)

同一仓里并存三套互不一致的"格式事实",引用时必须先声明取哪一层:

| 层 | 是什么 | 状态 |
|---|---|---|
| **V-HEAD** | `ab2f4ab` 的 `build_model.py`/`abstraction.py` 现行代码语义 | 学习/导出通道语法完整可信;监控通道损坏(坑1) |
| **V-产物** | 仓内现成 `embodied/dtmcs/`、`autonomous_vehicle/dtmcs/` 的 ~180 组三件套 | **旧版代码生成**,与 V-HEAD 在 ≥8 个格式点上不同(§6.3 对照表) |
| **V-README** | README L99-133 宣称的六方法接口、`safereach.embodied_build` 入口 | 与代码不符(teardown 坑2/坑10),**不要按它写对接代码** |

本笔记默认描述 **V-HEAD**(T5 复用的就是这层代码);V-产物差异集中列在 §6.3。

---

## ① 管线总览:格式在哪些关口发生

```text
原始 trace(每条对话/episode 一个观测序列)
   │  §2 输入契约:List[List[obs]],末尾哨兵 FINISH="finish"
   ▼
Abstraction.encode(obs) → 位串状态 "0101…"          §3 状态编码
   ▼
build_model(logs, abs, alpha) → model dict           §4 内存模型五键
   ▼
store_model(model, dir, abs) → 三件套落盘            §5 model.json / abstraction.json
   ▼                                                 §6 dtmc.prism 文法(可照抄样例)
prism CLI:prism dtmc.prism -pf "PCTL"               §7 属性文法与调用
   ▲
unsafe 状态集:谓词掩码 → {s=i|s=j…}                 §8 unsafe 集构造
```

---

## ② 输入契约:logs 与观测

### 2.1 build_model 的直接输入(`build_model.py:17`)

```python
def build_model(logs: List[List[Any]], abs: Abstraction, alpha=1.0)
```

- `logs`:观测序列的列表。**一条 trace = 一个 `List[obs]`**;`obs` 类型完全自由,只要 `abs.encode(obs)` 认识它。
- 末尾哨兵:具身入口在每条 log 末尾 `append(FINISH)`(`embodied/build.py:19`),`FINISH = "finish"`(`abstraction.py:4`)。哨兵会成为一个真实状态(终态),`encode` 必须特判透传(§3.4)。
- 相邻对计数(`build_model.py:35-41`):对每条 trace 的相邻状态对 `(s_t, s_{t+1})` 累加 `transition_counts[i][j]`;自环(连续相同位串)照常计数。

### 2.2 具身域盘面格式(照抄用,`embodied/build.py:7-24`)

一个任务目录 = 若干 trace 文件 + 一个谓词来源文件:

```text
<log_dir>/
├── *.json      # 每文件一条 trace:{"s_trans": [{"state": <obs>}, ...], ...}
│               #   log = [o["state"] for o in obj["s_trans"]] + [FINISH]
└── spec        # JSON 数组,自动构造谓词的输入(§3.3)
```

### 2.3 T5 对接约定(建议)

- 一条对话 = 一条 log;一个观测 = 一轮(或一窗)的快照 `dict`,如 `{"late_night": true, "dependence_score": 0.7, "turns_since_boundary": 3, ...}`。
- **观测字段硬约束**:`AtomicPredicate.state_eval` 直接 `observation[self.lhs]`(`predicate.py:49-52`),**无默认值,缺键即 KeyError** → 谓词表所有 `lhs` 字段必须在每个快照里齐全,trace 导出器负责补全。
- 时间窗谓词(持续 n 轮/深夜连续 T 分钟)不进抽象层:先按 teardown §3.5 的 clock 注入预处理(`autonomous_vehicle/monitor.py:492-526` 模板)把"距触发已 k 步"写成普通观测变量,谓词退化为普通原子(如 `t_dep<=K`)。
- 反面教材:`EmbodiedAbstraction.encode` **就地改写**输入观测(`embodied/abstraction.py:57-59` 清洗 `parentReceptacles`)——CompanionAbstraction 不要复制这个模式,清洗放 trace 导出器。

---

## ③ 状态编码:谓词表 → 位串

### 3.1 谓词 AST 与 JSON 形状(`predicate.py`)

三类节点,全是 pydantic BaseModel,`.dict()` 即 JSON 形状:

```jsonc
// AtomicPredicate(predicate.py:39):observation[lhs] op rhs
{"neg": false, "lhs": "late_night", "op": "==", "rhs": true}
// op ∈ {"==","!=",">","<",">=","<="}(OP_MAP,predicate.py:11-18);neg=true 时按 NEGATE_OP 取反义 op

// BinaryPredicate(predicate.py:55):and/or 二叉,可嵌套
{"lhs": {...AtomicPredicate...}, "op": "and", "rhs": {...}}

// QuantifiedPredicate(predicate.py:72):观测是"对象列表"时的 exist/all 包装(具身域用)
{"quantifier": "exist", "predicate": {...Atomic 或 Binary...}}
```

- **T5 简化**:对话观测是单 dict 不是对象列表 → 直接用 Atomic/Binary(`state_eval(observation)` 收 dict),**不需要 Quantified 包装**;若谓词逻辑复杂,teardown §6.2 已确认可以整个绕过 `predicate.py`,在 encode 里写 Python 布尔函数。
- 谓词的**规范名**(interpretation/filter 用):`convert_to_bool_var(lhs, op, rhs) = f"{lhs}_{op}_{rhs}"`(`autonomous_vehicle/abstraction.py:98-99`),如 `"late_night_==_True"`。谓词表建一列存此名。

### 3.2 位串规则(`embodied/abstraction.py:53-69`)

- `encode(obs) -> str`:**按谓词列表顺序**逐个求值,真=`'1'` 假=`'0'`,拼接成定长位串。
- **顺序即 schema**:`EmbodiedAbstraction.__init__` 注释"order matters"(L32-34);位串第 k 位 = 谓词表第 k 行。**谓词表 v0 必须冻结行序并显式加 `bit_index` 列**;改行序 = 之前学的所有 DTMC/解释全部作废。
- 状态空间 = **经验观测到的位串集合**(`build_model.py:21-27`),不做 2^n 全枚举(AV 域另有 z3 剪枝全枚举,teardown §3.2,T5 v0 不需要)。

### 3.3 spec → 谓词自动构造(具身域参考,`embodied/build.py:27-48`)

对 spec 数组每个元素(如 `{"objectType":"Mug","isBroken":true}`):`objectType` 键 → `objectType==<值>`;`parentReceptacles` 键(单元素列表)→ `parentReceptacles==<整个列表>`(**列表相等比较**);其余键 → `<键>==True`;每个原子包一层 `exist`,最后追加全键合取谓词。位数 = Σ(每 spec 键数+1)。T5 不走自动构造(谓词表是手工资产),此节仅为读懂现成产物的位数。

### 3.4 两个必守特判

- `encode(FINISH) → "finish"` 原样透传(`embodied/abstraction.py:54-55`);
- `valid_trans(FINISH, ·) = False`(终态无出边,`embodied/abstraction.py:106-110`)。CompanionAbstraction 在此之上再加关系域剪枝(如"已转介人工"吸收态),这是具身域没做、AV 域做了、**T5 应做**的部分(teardown §6.1)。

### 3.5 状态索引的再现性坑

`get_state_idx` 收到的是 **set**(`build_model.py:19,31`),具身实现按 set 迭代序编号(`embodied/abstraction.py:42-45`)→ **同批数据两次运行,索引映射可能不同**(Python 字符串哈希随机化)。后果:unsafe 状态集、缓存的 PCTL 公式、init 序号全部随运行漂移。**T5 修正:`get_state_idx` 内先 `sorted(states)` 再枚举**(一行,收益极大)。

---

## ④ DTMC 学习输出:model dict 五键(`build_model.py:77-84`)

```jsonc
{
  "states":            ["000", "010", "011", "finish"],        // list(state_space),顺序=编号顺序
  "state_index":       {"000": 0, "010": 1, "011": 2, "finish": 3},
  "state_interpret":   {"000": <decode(s) 的返回>, ...},        // 形状由子类 decode 决定,见 §5.3
  "transition_counts": {"0": {"0": 1, "1": 2}, ...},            // 稀疏:只存非零行/非零项;键是整数索引(json 后成字符串)
  "transition_probs":  {"0": {"0": "2.0/7.0", "1": "3.0/7.0", ...}, ...}   // 概率是【字符串分数】,直接进 PRISM
}
```

概率字符串的生成规则(`build_model.py:53-73`,格式相关三条):

1. **分母** `denom = n_i + Σ_j α·[valid_trans(s_i,s_j)]`(= 论文的 `n_i + k_i·α`);**分子** `n_ij + α` 无条件适用——含非法转移(**与论文偏差**,teardown 坑8)。T5 若实现了真剪枝的 `valid_trans`,必须把分子 α 条件化(`if abs.valid_trans(...)` 才 `+alpha`,并跳过非法项),否则概率行不归一;建议 build 后加 `assert` 每行和=1。
2. **浮点书写**:`alpha=1.0` 是 float → HEAD 写出 `"385.0/393.0"` 样式(不约分;`fractions.Fraction` 在 L7 import 了但没用——旧版遗迹)。PRISM 能解析,但建议 T5 用 `Fraction(n+α_int, denom_int)` 写成 `"385/393"`(现成产物即此风格,更可读可验)。
3. **零出边兜底**:denom=0(如 FINISH)→ 整行替换为自环 `{i: "1.0"}`(L72-73)。

---

## ⑤ 落盘三件套:store_model(`build_model.py:86-93`)

### 5.1 调用契约

```python
store_model(model, dir, abstraction)   # dir 必须带尾斜杠!内部是 dir + "model.json" 字符串拼接
```

且内部 `os.mkdir`(非 makedirs)——嵌套目录需预建。写出 `model.json`(§4 原样 json.dumps)+ `abstraction.json` + `dtmc.prism`。

### 5.2 abstraction.json(V-HEAD:`embodied/abstraction.py:38-40`)

= 谓词 dict 的 JSON 数组,**数组序 = 位序**,即编码 schema 本体:

```json
[
  {"neg": false, "lhs": "late_night", "op": "==", "rhs": true},
  {"neg": false, "lhs": "dependence_score", "op": ">", "rhs": 0.6},
  {"neg": false, "lhs": "boundary_request", "op": "==", "rhs": true}
]
```

**坑**:HEAD 的读取端 `embodied/monitor.py:11-18` `load_abstraction` 仍在读旧三键格式 `{"objectTypes":[…],"keys":[…],"parentReceptacles":[…]}`(仓内现成产物即旧格式)——**新格式的 loader 在 HEAD 不存在,T5 自写**(反序列化数组 → `AtomicPredicate(**d)` → 按序重建谓词列表,~15 行)。

### 5.3 state_interpret 两种形状

- 具身 HEAD `decode`:`[[<谓词dict>, "0"], [<谓词dict>, "1"], …]` 对列表(`embodied/abstraction.py:71-80`)——够调试,**不够 filter 用**;
- AV HEAD `get_state_interpretation`:`{<lhs_op_rhs>: true/false, …}` 字典(`autonomous_vehicle/abstraction.py:233-247`)——§8 的可用 `filter` 消费的就是这个。**T5 采用 AV 形状**。

---

## ⑥ dtmc.prism 文法(可照抄样例)

### 6.1 V-HEAD 发射文法(`build_model.py:95-121`,逐字符对照)

```text
dtmc\n
\n
module dtmc_model\n
\n
    s : [0..{K}] init {initial_state};\n          ← K=len(states);域含 K+1 个值,索引 K 是"理论上未观测"虚拟态
\n
    [] s={i} -> {p1} : (s'={j1}) + {p2} : (s'={j2}) …;\n    ← 每观测状态一行;p=字符串分数;项序=state_space 迭代序
    [] s={K} -> 1.0: (s'={K});\n                  ← 虚拟态自环(注意"1.0:"后无空格——L120 原样)
\n
endmodule\n
```

### 6.2 可照抄样例三份

**样例 A|toy 全链路(V-HEAD 语义,手工构造可复算)**。谓词表 3 行:`late_night==True`(bit0)、`dependence_score>0.6`(bit1)、`boundary_request==True`(bit2);两条对话:

```text
T1: 000 → 010 → 010 → 011 → finish        T2: 000 → 000 → 010 → finish
计数:n(000→000)=1  n(000→010)=2  n(010→010)=1  n(010→011)=1  n(010→finish)=1  n(011→finish)=1
索引(按 sorted):000=0, 010=1, 011=2, finish=3;K=4;valid_trans:除 finish 外全合法(k_i=4)
```

HEAD `export_dtmc_to_prism` 对此模型的**精确输出**(α=1.0;分母 n_i+4;分子 n+1):

```text
dtmc

module dtmc_model

    s : [0..4] init 0;

    [] s=0 -> 2.0/7.0 : (s'=0) + 3.0/7.0 : (s'=1) + 1.0/7.0 : (s'=2) + 1.0/7.0 : (s'=3);
    [] s=1 -> 1.0/7.0 : (s'=0) + 2.0/7.0 : (s'=1) + 2.0/7.0 : (s'=2) + 2.0/7.0 : (s'=3);
    [] s=2 -> 1.0/5.0 : (s'=0) + 1.0/5.0 : (s'=1) + 1.0/5.0 : (s'=2) + 2.0/5.0 : (s'=3);
    [] s=3 -> 1.0 : (s'=3);
    [] s=4 -> 1.0: (s'=4);

endmodule
```

配套 model.json(节选;state_interpret 按 §5.3 AV 形状):

```json
{"states": ["000","010","011","finish"],
 "state_index": {"000":0,"010":1,"011":2,"finish":3},
 "state_interpret": {"000": {"late_night_==_True": false, "dependence_score_>_0.6": false, "boundary_request_==_True": false}},
 "transition_counts": {"0":{"0":1,"1":2},"1":{"1":1,"2":1,"3":1},"2":{"3":1}},
 "transition_probs": {"0":{"0":"2.0/7.0","1":"3.0/7.0","2":"1.0/7.0","3":"1.0/7.0"},
                      "1":{"0":"1.0/7.0","1":"2.0/7.0","2":"2.0/7.0","3":"2.0/7.0"},
                      "2":{"0":"1.0/5.0","1":"1.0/5.0","2":"1.0/5.0","3":"2.0/5.0"},
                      "3":{"3":"1.0"}}}
```

**样例 B|仓内现成产物原文**(V-产物层,`src/safereach/embodied/dtmcs/merged_log_raw_t3/dtmc.prism` 全文,5 状态,states=["100","101","110","111","finish"],finish=4):

```text
dtmc

module dtmc_model

    s : [0..4] init 0;

    [] s=0 -> 385/393 : (s'=0) + 1/393 : (s'=1) + 2/131 : (s'=2) + 1/393 : (s'=4);
    [] s=1 -> 1/4 : (s'=0) + 1/4 : (s'=1) + 1/4 : (s'=3) + 1/4 : (s'=4);
    [] s=2 -> 3/8 : (s'=0) + 3/8 : (s'=2) + 1/8 : (s'=3) + 1/8 : (s'=4);
    [] s=3 -> 1/4 : (s'=1) + 1/4 : (s'=2) + 1/4 : (s'=3) + 1/4 : (s'=4);
    [] s=4 -> 1 : (s'=4);

endmodule
```

**样例 C|T5 手写最小模板**(建议的规范化风格:既约分数+虚拟态+注释):

```text
dtmc

module dtmc_model

    // bit0=late_night  bit1=dependence  bit2=boundary_request ; 3=finish ; 4=unseen
    s : [0..4] init 0;

    [] s=0 -> 2/7 : (s'=0) + 3/7 : (s'=1) + 1/7 : (s'=2) + 1/7 : (s'=3);
    [] s=1 -> 1/7 : (s'=0) + 2/7 : (s'=1) + 2/7 : (s'=2) + 2/7 : (s'=3);
    [] s=2 -> 1/5 : (s'=0) + 1/5 : (s'=1) + 1/5 : (s'=2) + 2/5 : (s'=3);
    [] s=3 -> 1 : (s'=3);
    [] s=4 -> 1 : (s'=4);

endmodule
```

### 6.3 V-产物 vs V-HEAD 格式对照(照抄样例 B 前必看)

| 格式点 | V-产物(仓内现成) | V-HEAD(现在重跑会得到) |
|---|---|---|
| 状态域 | `s:[0..K-1]`,无虚拟态(样例 B `[0..4]`=5 个真实状态) | `s:[0..K]` + 虚拟态 K 自环 |
| 概率书写 | 既约分数 `"2/131"`(Fraction)〔反推〕 | 浮点串 `"6.0/394.0"`,不约分 |
| 分子 α | 仅合法转移(样例 B s=0 行和恰=1 且缺 s'=3 项)〔反推〕 | 无条件 +α(坑8,与论文偏差) |
| 行剪枝 | 非法转移整项缺席(`100→111` 双位翻转=非原子,被旧 valid_trans 剪掉)〔反推〕 | 具身域无剪枝(`valid_trans≡True`) |
| finish 自环 | `1 : (s'=4)` | `1.0 : (s'=3)`(兜底行)/虚拟态 `1.0:` |
| model.json 键 | 位串字符串键,无 transition_counts | 整数索引键(json 后为 `"0"…`),含稀疏 counts |
| abstraction.json | 旧三键 `{objectTypes,keys,parentReceptacles}` | 谓词 dict 数组(§5.2) |
| state_interpret | 具身:对象状态列表;AV:`[谓词串, bool]` 对列表 | 具身:`[谓词dict, bit]` 对;AV:`{lhs_op_rhs: bool}` 字典 |
| init 值 | AV `s1/dtmc.prism` 竟为 `init 39` | ——(这是 `runtime_monitor` 就地改写 init 的**副作用实锤**,§7.3) |

结论:**做格式对齐测试用样例 A(可复算);做 PRISM 冒烟用样例 B(仓内现成);写 T5 导出器按样例 C 风格 + §6.1 文法**。

---

## ⑦ 属性文法(PCTL)与 PRISM 调用

### 7.1 属性文法的真实状态

- `ctl.py` 定义了 `Until/Next/Finally/Always`(+`All/Exist` 包装)的 AST,`Finally/Always` 带 `bound` 字段,`__str__` 产出 `F<=k p` / `G<=k p` 样式——**但 AST→PCTL 翻译层是半成品**:`path_to_pctl` 的 Until 分支两次引用 `predicate1`(`runtime_monitor.py:62-64`)、`predicate_to_state` 是空 `pass`(L74-75)。
- **事实上的属性文法 = 手拼 PRISM 字符串**,原子只有一种:`s=<idx>`;unsafe 集拼 `(s=i|s=j|...)`(被注释的原始逻辑 `runtime_monitor.py:39-43`)。**T5 直接拼字符串,不要接 ctl.py 的翻译层**。

### 7.2 规范查询模板(T5 直接照抄)

```text
P=? [ F (s=2|s=5) ]          ← 无界可达 unsafe(README:83 的原语义;论文 P_safe 的补)
P=? [ F<=10 (s=2|s=5) ]      ← k 步有界(T5 主用:04_DERIVATION 发现①——无安全 BSCC 时无界式 P_safe≡0,必须用有界式)
P=? [ G !(s=2|s=5) ]         ← P_safe 直查(HEAD 损坏行 L46 想拼的就是它;与第一式互补)
P<0.1 [ F (s=2|s=5) ]        ← 布尔判定式(阈值写进公式;论文 README:83 形态)
filter(printall, P=? [ F (s=2|s=5) ], true)   ← 一次跑出【所有状态】的值 → 离线建 cache 表(替代逐状态改 init;语法待复现窗实测)
```

### 7.3 调用与解析契约(`runtime_monitor.py:9-59`)

- 命令:`../prism/bin/prism {dtmc_path} -pf "{formula}"`(L47)——**相对路径,cwd 必须是 `src/`**;仓库移动后先重跑 `prism/install.sh`(teardown §4.3)。
- 结果解析:正则 `Result:\s*([0-9.]+)` 抓 stdout(L50-53),取 float。
- "以当前状态为初态"的实现 = **正则就地改写 dtmc.prism 的 init**(L21-28,模式 `s\s*:\s*\[\d+\.\.\d+\]\s+init\s+\d+;`)——有文件副作用与重入风险(坑7;AV `s1/dtmc.prism` 的 `init 39` 即残留)。**T5 弃用**:离线用 7.2 的 filter 式(或逐状态临时副本)预计算全状态表,在线 O(1) 查 dict——这正是论文声称、HEAD 缺失的 cache(坑7)。
- 运行时未见过的位串:`state_idx[current_state]` 直接 KeyError(L13);虚拟态 K 只有自环、查出来 P[F unsafe]=0 是**危险的乐观值**——T5 约定:未知状态一律保守处理(返回 prob=1.0 或触发降级),不要映射到虚拟态。
- 冒烟命令(P0 网关,**本窗未运行**):

```bash
cd /mnt/d/MyResearch/external/Pro2Guard
./prism/bin/prism src/safereach/embodied/dtmcs/merged_log_raw_t3/dtmc.prism -pf 'P=? [ F s=4 ]'
# 预期 stdout 末尾:Result: <0-1 浮点>(需 Java;详见 teardown §5-P0)
```

### 7.4 阈值语义

θ 不进公式(在线钩子里 `prob > threshold` 比较,`controlled_agent_excector.py:107`);各档取值与语义速查见 teardown §3.4,不在本笔记复述。

---

## ⑧ unsafe 状态集构造(属性的另一半)

两层做法,**T5 用符号层**:

- **观测层**(具身现状):任务 spec 的 `unsafe_state` JSON 直接对原始观测求值(`embodied/eval.py:50-66` `eval(observation, specs)`,含 parentReceptacles 特判)——绕过了符号状态,只用于离线统计,与 DTMC 无关。
- **符号层**(AV 侧,**能用的版本**):`av_monitor.py:42-63` `truth_table(interp, pred)` + `filter(state_interp, pred)`——对 model.json 的 `state_interpret`(§5.3 AV 字典形状)逐状态求谓词真值,返回满足的状态列表,再 `[state_idx[s] for s in states]` 转索引 → 拼 `(s=i|s=j|…)`。注意 `EmbodiedAbstraction.filter` 是坏的(坑11:`self.predicate` 笔误 + product 未 join),**别用具身版**。

T5 流程固定为:谓词表 unsafe 列给出掩码(如 `boundary_request_==_True: true`)→ `filter` 扫 `state_interpret` → 索引集 → PCTL 字符串。~20 行,参照 av_monitor 版。

---

## ⑨ T5 谓词表对接检查表(交付口)

**谓词表 v0(16 个带时间窗谓词,companion-survey/14_academic 域)每行需补齐的管线字段**:

| 谓词表列 | 管线要求 | 依据 |
|---|---|---|
| `bit_index` | 冻结行序=位序,改序作废所有已学模型 | §3.2 |
| `lhs / op / rhs` | op ∈ OP_MAP 六种;lhs 必须是快照 dict 的键(每快照齐全,无默认值) | §2.3/§3.1 |
| `bool_var` | `f"{lhs}_{op}_{rhs}"` 规范名(interpretation/filter 键) | §3.1 |
| 时间窗参数 | 不进抽象层;clock 注入预处理转普通变量后再写原子 | §2.3 |
| `unsafe` 掩码 | 供 §8 filter 构造 unsafe 集 | §8 |
| `absorbing`(可选) | 供 valid_trans 剪枝(吸收态/不可跳变);启用剪枝必须同步条件化分子 α | §3.4/§4-1 |

**CompanionAbstraction 的六项接口义务**(基类 5 抽象方法 `abstraction.py:6-26` + 1 项 de facto):

1. `encode(obs)->str` 位串(FINISH 透传;不改写输入);
2. `decode(state)`(调试用,随意);
3. `valid_trans(s1,s2)->bool`(FINISH→False;关系域剪枝);
4. `get_state_idx(states)`(**先 sorted 再枚举**,§3.5);
5. `get_state_interpretation(states)`(AV 字典形状,§5.3);
6. `to_json()`——**不在 ABC 里但 `store_model` 硬调用**(`build_model.py:92`),漏写 AttributeError。

**复用/重写边界**(与 teardown §6 一致,格式视角复核):`build_model/store_model/export_dtmc_to_prism` 三函数与域无关,照用;`runtime_monitor` 按 §7.3 重写(预计算表);若求"与论文一致"的复现口径,再打两针:分子 α 条件化 + 概率行归一断言(§4-1)、分数 Fraction 化(§4-2)。

---

**关联**:T5 提案 §9"复现即预研"行(`research/map/proposals/T5_companion_prob_shield.md`)| teardown 复现路线 §5(P0-P4)| 本目录 README"待补 05_REPRODUCTION"(2026-08-14 01:06 起 LP-01 复现窗已在途)。
**配套**:使用手册 `GUIDE_addendum_dtmc_prism.md`(按场景用法)| 维护手册 `MAINTENANCE_addendum_dtmc_prism.md`(更新触发器/机械验证/遗留台账)| 交接档 `progress/handoff/2026-08-14__lightwindow-probguard-dtmc-format__handoff.md`(溯源)。
**最后更新**:2026-08-14
