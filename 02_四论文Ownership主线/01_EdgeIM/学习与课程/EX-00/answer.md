六个事件？ok

有序对-集合-Rtmp

## 3. Algorithm 1（读，20 分钟）

下面是论文 p.407（PDF 第 4 页）左栏 Algorithm 1 的逐行转录，符号照抄原文。第 1 站你会拿 PDF 对照它；这一站只需要能照着跑。

```
Algorithm 1: Feature-Preserving Sampling

Input : cases set = {σ1, σ2, …, σn}
Output: Filtered D′, Global Features (S, E, R)

 1  Sort L by ⟨CaseID, Timestamp⟩ to obtain ordered cases Case_ord——这句是什么意思
 2  Initialize S ← ∅, E ← ∅, R ← ∅——初始化
 3  for each trace σ in Case_ord do——对每一个trace中……？
 4      Extract s ← σ[0], e ← σ[−1], Rtmp ← {(σ[k], σ[k+1]) | 1 ≤ k < |σ|}——没看懂。。
 5      if (s ∉ S) ∨ (e ∉ E) ∨ (Rtmp ⊄ R) then——针对每个新的s、e、Rtmp时候在集合里的判断
 6          D′ ← D′ ∪ {σ}          // Add log to D′——这里直接有D'了吗？
 7          S ← S ∪ {s}
 8          E ← E ∪ {e}
 9          R ← R ∪ Rtmp
10      end
11  end
12  return D′, S, E, R
```

读的时候在每一行旁边写两个字：这一行**读**了哪些变量、**改**了哪些变量。三个小问题，答案写进作答文件：

- 3.1 第 2 行初始化了三样东西。第 6 行往 D′ 里放东西——D′ 是在哪一行初始化的？如果让你补这一行，你写什么？
好像没有初始化，第二行初始化？D' ← ∅

- 3.2 第 4 行 Rtmp 的下标范围原文写的是 `1 ≤ k < |σ|`，而起点是 `σ[0]`。按这个范围**逐字**去取 ⟨a,b,c,e⟩ 的相邻对，会得到哪几对、漏掉哪一对？（按 §2 的定义应该是哪几对——以定义为准，这一站后面都按定义算。）
第一个会漏吧，a→b。得到bc,ce

- 3.3 第 5 行三个条件之间是 ∨（或）。用一句话说：什么情况下一条 trace 会**被滤掉**？
trace的s e rtmp都在集合里能找到？



## 4. 练习日志 L0（算，60 分钟）

**任务 1**：写出 c1–c6 六条 trace。（c4 要按时间排。）

c1:ab bc ce
c2:ac cd de
c3:ab bc cd de 
c4:ab bc cb ce
c5:ac cd de 
c6:bc ce

**任务 2**：给每条 trace 算 s、e、Rtmp——一张 6 行表。c4 的 Rtmp 有几个元素？
ID S E R 
c1 a e ab bc ce 
c2 a e ac cd de
c3 
c4 a e cb 
c5 
c6 b e 

**任务 3 · 先预测（写在跑之前，不许改）**：

- (p1) 按 c1→c6 的顺序跑，你猜留下几条？哪几条？
顺序：
ID S E R 
c1 a e ab bc ce 
c2 a e ac cd de
c3
c4 cb
c5 
c6 b

留四条，过滤三条

- (p2) 有没有哪一条，不管顺序怎么排都**一定留**？
c6

- (p3) 有没有哪一条，不管顺序怎么排都**一定被滤**？
c3

**任务 4 · 正序跑（c1→c6）**：一张"状态表"，一条 case 一行。这张表是本站的核心——它把"状态"变成一个你必须写下来的东西：


| 进来的 case | 跑它**之前** S / E / R | s∉S? | e∉E? | Rtmp⊄R?（写出不在 R 里的那些对） | 留/滤 | 跑它**之后** S / E / R |
| -------- | ------------------ | ---- | ---- | --------------------- | --- | ------------------ |
| c1       | ∅ / ∅ / ∅          | a    | e    |ab bc ce              |留  |a / e /ab bc ce           |
| c2       | a / e / ab bc ce  | …    | …    | ac cd de                   | 留  | a / e / ab bc ce ac cd de    |
| c3       | a / e / ab bc ce  ac cd de| …    | …    | …                     |滤   | a / e / ab bc ce ac cd de  |
| c4       | a / e / ab bc ce  ac cd de| …    | …    | …                     | 滤  | a / e / ab bc ce ac cd de |
| c5       |  a / e / ab bc ce  ac cd de| …    | …    | …                     | 滤  | a / e / ab bc ce ac cd de |
| c6       |  a / e / ab bc ce ac cd de  | b    | …    | …       | 留  |  a b / e / ab bc ce ac cd de |


跑完写：D′ = { }，最终 S、E、R，以及 |R|。
——这里应该怎么写？
D′ = { a b/ e / ab bc ce ac cd de }
S = {a b}
E = {e}
R = {ab bc ce ac cd de }
|R|——6


**任务 5 · 逆序跑（c6→c1）**：把 CaseID 反过来编号（c6 叫 c1′……c1 叫 c6′），第 1 行排序之后自然就是这个顺序。同样一张状态表。跑完写 D′、S、E、R。

逆序：
ID S E R 
c1' b e bc ce
c2' a e ac cd de 
c3' a e ab bc cb ce
c4' a e ab bc cd de 
c5' a e ac cd de
c6' a e ab bc ce 

| 进来的 case | 跑它**之前** S / E / R | s∉S? | e∉E? | Rtmp⊄R?（写出不在 R 里的那些对） | 留/滤 | 跑它**之后** S / E / R |
| -------- | ------------------ | ---- | ---- | --------------------- | --- | ------------------ |
| c1'       | ∅ / ∅ / ∅          | b    | e    |bc ce              |留  |b / e / bc ce           |
| c2'       | b / e /  bc ce  | a    | …    | ac cd de                   | 留  | a b / e / bc ce ac cd de    |
| c3'       | a b / e / bc ce ac cd de| …    | …    | ab                    |留   | a b / e / ab bc ce ac cd de|
| c4'       |  a b / e / ab bc ce ac cd de| …    | …    | …                     | 滤  | a b / e / ab bc ce ac cd de|
| c5'       |  a b / e / ab bc ce ac cd de| …    | …    | …                     | 滤  |  a b / e / ab bc ce ac cd de |
| c6'       |  a b / e / bc ce ac cd de | …    | …    | …                     | 滤  |  a b / e / ab bc ce ac cd de |


**任务 6 · 两张表对照**：

- (a) 最终 S、E、R 相同吗？|D′| 相同吗？

SER相同，|D′| 不同

- (b) c2 和 c5 是同一条 trace。两次各留了谁？一句话：由什么决定？
留了先输入的，输入顺序

- (c) c3 两次都被滤了。它跟谁重复？——不跟任何一条重复。那它为什么被滤？指出它的每一对相邻对分别在哪条**先到的** case 里出现过
（这里这题在写的过程中就能看得出来了吧，感觉没必要再写一遍）——话说问题要不要稍微有点拓展性？🤔

- (d) c6 的每一对相邻对，在正序里都早就见过了。那它为什么留？
？留了吗？，顺序的吗？顺序的是因为s不一样啊

- (e) 第 5 行的判据本身不看顺序——它就是三个"在不在"。那"看顺序"是从哪一行进来的？（提示：看状态表"之前"那一列，两张表同一个 case 的这一列一样吗？）
——不一样

- (f) 回头给 (p1)(p2)(p3) 打 ✓/✗，错的写一句为什么


**任务 7 · 改一个条件（先预测再跑）**：

- (a) 把第 7–9 行搬到 if 外面——每条 case 不管留不留都并入 S、E、R。正序重跑，D′ 变不变？最终 S、E、R 变不变？先写预测，再挑一种顺序验证，然后用一句话说为什么

不变吧？所以D'是什么这样是什么意思，直接并入不删去重复的吗？不删就变。

- (b) 把第 5 行改成只看 `Rtmp ⊄ R`（不看 s、e）。正序跑，谁的命运变了？

顺序的c6。

**任务 8 · 另一个程序（20 分钟）**——这一题回答"为什么没有 K"：

> **程序乙**：给定一个数 K。对每条 case 算一个分数（比如 |Rtmp|），按分数从高到低排，取前 K 条。

- (a) 程序乙里，"最后留几条"由谁决定？是跑之前就知道，还是跑完才知道？Algorithm 1 呢？

最后留几条就是K，跑之前就知道，Alg是跑完知道

- (b) 你能不能通过**只改输入**，让 Algorithm 1 在 L0 上恰好留 2 条？留 6 条？（提示：任务 4、5 各留了几条；你手里能改的输入只有 CaseID 的编号）

删了c6

- (c) 如果硬给 Algorithm 1 加一条"留满 3 条就停"（K=3），正序跑，D′ 是哪 3 条？此时最终的 S、R 跟任务 4 的比，**少了什么**？
c1 c2 c6

- (d) 一句话：Algorithm 1 里 |D′| 是输入还是输出？程序乙里 K 是输入还是输出？
输出。程序乙里面是输入
