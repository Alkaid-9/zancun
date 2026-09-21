# A4 EX-05 定点 CS 基础

状态：`JIT-ONLY / NO-GENERAL-COURSE / NON-COURSE-MICRO-EXERCISES`

只在当前代码卡住时读对应小节。每节的微练习都不使用 EX-05 正式数据，不给标准答案。

## 1. tuple 和 list

- `tuple` 是固定顺序容器，通常用于不希望就地修改的事件序列。
- `list` 可以 `append`、切片和就地更改；复制后打乱能避免改原顺序。
- 当前对象：`own.py:33-48,93-96`。

微练习：用 `("red", "blue", "red")` 和它的 list 副本演示“副本可乱序，原 tuple 不变”；自己说明为什么需要副本。

## 2. dataclass 和 Mapping

- `@dataclass` 把有名字段的数据契约放在类定义上；`frozen=True` 阻止实例属性被普通赋值改写。
- `Mapping[K, V]` 表示“可按键读值”的接口，不承诺必然是可修改的 `dict`。
- 当前对象：`pilot.py:38-95`。先凭记忆写 representation，再打开这些行核对；不从公开题面的预填字段倒签。

微练习：定义一个冻结的 `Book(title, pages)`，再用一个 `Mapping[str, int]` 记录两本书的页数。试图改冻结实例，只记报错类型和你的解释。

## 3. 函数重定义

Python 文件从上到下执行。同名 `def` 再出现后，后续查找到的是新函数；但在重定义之前已经执行的调用，用的是旧函数。

- 当前对象：`test_invariants.py:8-20` 与 `:79-92`。

微练习：写两个同名 `label(x)`，在两次定义之间和之后各调用一次。先预测两行输出，再运行。

## 4. oracle 和 invariant

- oracle 是独立判定规则；它不应从被测算法的输出倒推真值。
- invariant 是在明确的输入变化范围内应保持的性质。有限输入全过只支持这些输入。
- 当前对象：`test_invariants.py:43-64`。

微练习：对一个三角形的三个顶点同时平移一个向量，设计检查“三条边长不变”的 invariant；再构造一个边长不变但位置已变的例子，说明主张上限。

## 5. seed

seed 固定伪随机流的起点。“同 seed 可重现”还依赖相同实现、Python/库版本和调用顺序。

- 当前对象：`own.py:27,93-99`；`pilot.py:101-110,177-220`。

微练习：对 `["north", "east", "south", "west"]` 的两个独立副本用同一 seed 打乱，记录环境和结果；再改 seed 比较。

## 6. traceback

traceback 从调用链展示异常传播路径。先找最后一个自己/项目代码帧，再记录异常类型、消息和当时输入。traceback 定位失败点，不自动证明根因。

微练习：让 `lookup({"a": 1}, "b")` 产生一次未捕获错误，记录“异常类型 / 首个项目行 / 竞争解释”。

## 7. assert

`assert actual == expected, message` 是可执行检查。它只检查写下的布尔条件；条件选错时，“全过”也没意义。

- 当前对象：`test_invariants.py:58-61`。

微练习：对一个订单价格列表分别写“总数不变”和“总和不变”两个 assert，然后构造一个只能被其中一个抓住的错误。

## 8. Git diff

只读检查：

```sh
git -C /mnt/d/Alkaid/Desktop/zancun status --short
git -C /mnt/d/Alkaid/Desktop/zancun diff -- '02_四论文Ownership主线/01_EdgeIM/学习与课程/EX-05'
git -C /mnt/d/MyResearch/MAS_Safety_Project diff -- 'learning/training/lu-edgeim-algo1/EX-05' 'research/edgeim_sampling_audit/src/pilot.py'
```

这些命令只说明工作树差异，不证明代码正确或本人 PASS。

微练习：在临时目录准备 `before.txt` 和 `after.txt`，只改一个虚构配额数字。先预测 diff 的行首标记，再用 `git diff --no-index before.txt after.txt`核对，并解释“看到差异”和“改动正确”为什么是两件事。
