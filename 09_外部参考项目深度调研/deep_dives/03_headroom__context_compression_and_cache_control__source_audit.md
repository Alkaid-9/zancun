# L3 源码深度剖析 03 · headroomlabs-ai/headroom 本地上下文压缩与缓存边界守卫机制

- **审查对象**：`headroomlabs-ai/headroom`
- **审计深度**：**L3 源码与底层实现级（Rust 核心代码静态审查）**
- **本地源码凭证**：
  - `receipts/sources/headroom/lib.rs`（Rust 底层 crate 架构定义）
  - `receipts/sources/headroom/cache_control.rs`（15.4 KB 缓存控制标记解析器与冻结边界计算器）
  - `receipts/sources/headroom/compression_benchmark.py`（33.0 KB 真实压缩率与语义损失基准）

---

## 1. 核心质疑与除魅：5x~20x 压缩到底是真突破还是噱头？

市面有很多声称“上下文压缩”的项目，常常是通过粗暴截断字符串或删减行号来实现。这会导致：
1. **代码行号失真**：Agent 根据压缩后的代码去修改文件，行号全错，发生灾难性代码覆盖。
2. **破坏 Prompt Caching**：修改了历史消息，导致 Anthropic/OpenAI 的 Prompt Cache Key 改变，缓存命中率直接归零，Token 费用不降反增 3~4 倍！

**Headroom 源码审查结论**：
Headroom 是经得起严肃工业级推敲的高质量系统。其核心逻辑完全用 **Rust 编写（`crates/headroom-core`）**，并且在设计上有着极其严苛的 **“缓存守卫不变式（Cache Guard Invariants）”**。

---

## 2. 核心源码逐行解剖：`cache_control.rs`（提示词缓存边界硬约束）

### 2.1 绝对不可触碰的冷冻区（The Frozen Prefix）
看 `cache_control.rs:1-18` 的核心设计哲学：
> *"Anthropic prompt caching pins a prefix of the request: every block up to and including the last cache_control marker is part of the cache key. Headroom's compressor must **never** modify any byte that's part of that prefix — doing so changes the cache key, drops the hit rate to 0, and silently torches the customer's bill."*

在 `cache_control.rs:109-133`，Rust 代码实现了 `compute_frozen_count`：
```rust
pub fn compute_frozen_count(parsed: &Value) -> usize {
    let mut highest_message_index: Option<usize> = None;

    // 1. 遍历 messages[*] 寻找所有用户显式标记的 cache_control
    walk_messages(parsed, &mut highest_message_index);

    // 2. 遍历 system 与 tools（这些字段默认属于无条件冷冻热区）
    walk_system(parsed);
    walk_tools(parsed);

    // 3. 将最高标记索引转换为 exclusive 冷冻下界：messages[0..=i] 绝对禁止压缩！
    highest_message_index.map(|i| i + 1).unwrap_or(0)
}
```

### 2.2 为什么严禁使用正则表达式？
看 `cache_control.rs:38-46` 的工程守则：
> *"Why no regex: Per the realignment build constraints, pattern detection uses parsers, not regex. We walk the parsed JSON tree via serde_json accessors only — that's both safer (no pattern-string typo risk) and faster (no compilation cost on the hot path)."*

它在 Rust 层面直接操作 `serde_json::Value` 的 AST 树指针，避免了传统正则在大文本流匹配时的灾难性回溯（ReDoS）和 CPU 飙升。

### 2.3 动态活跃区压缩（Live-Zone Compression）
- **冷冻区（Frozen Zone，`0` 到 `frozen_count`）**：保持字节级 100% 相同，直接吃满 Anthropic 的 `cache_read_input_tokens` 折扣（通常省 90% 成本）。
- **活跃区（Live Zone，`frozen_count` 之后）**：仅对最新产生的超大 Tool Output、终端构建错误、长日志进行基于 `kompress` 局部小模型的语义压缩（剔除冗余堆栈框架、合并空白符、提炼核心错误代码）。

---

## 3. 对我们系统的复用方案（可直接偷师的代码与架构）

| 偷师模块 | 对应源码文件 | 拟引入到本项目的哪部分 | 收益与解决的痛点 |
|---|---|---|---|
| **Cache-Safe 冻结边界计算** | `cache_control.rs` 中的 `compute_frozen_count` 逻辑 | 工作台底层代理或 MCP 中继层 | 彻底解决“压缩导致 Prompt Cache 穿透失效”的痛点，确保长程交互缓存命中率 > 80% |
| **Tool Output 差异化压缩策略** | `benchmarks/compression_benchmark.py` 的测试用例 | 两台文件与终端输出截断层 | 区分纯代码文件（保持原样）与调试日志（大幅提纯），在源头防止 429 额度报警 |
