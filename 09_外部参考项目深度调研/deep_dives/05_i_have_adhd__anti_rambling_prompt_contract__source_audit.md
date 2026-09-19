# L3 源码深度剖析 05 · ayghri/i-have-adhd 认知载荷优化与防废话提示词契约

- **审查对象**：`ayghri/i-have-adhd`
- **审计深度**：**L3 提示词契约与交互协议级（Prompt Engineering & Cognition Guard Static Audit）**
- **本地源码凭证**：`receipts/sources/i-have-adhd/SKILL.md`（7.2 KB 官方完整技能规范定义）

---

## 1. 核心定位：这不仅是“简短回答”，而是一套严格的认知防崩阻断器

在 Agent 辅助软件工程中，模型最致命的毛病就是**“废话多、铺垫长、总结啰嗦、核心结论深埋在文章中段”**。
每次模型回复：
- “好的！让我来思考一下您的认证流程，认证流程主要有三个部分……”（消耗 50 Tokens）；
- 结尾加上：“希望这些对您有所帮助！如果有任何疑问请随时告诉我！”（消耗 30 Tokens）。

在长程研发会话中，这种毫无信息量的社交套话不仅白白消耗成千上万的 Token，还会稀释有效上下文，诱发模型注意力漂移。

`i-have-adhd` 表面上叫“多动症友好”，本质上是目前业界**对大模型能动性（Agency）与信息密度约束最为严苛的系统级提示词契约**。

---

## 2. 核心源码解剖：十条铁律与发送前校验（Pre-send Check）

### 2.1 违禁词句与红线（Forbidden Patterns）
在 `SKILL.md:109-118`，白纸黑字列出了必须严格抹杀的三类句式：
- **禁止开场白（Forbidden Openers）**：
  `"Great question"`, `"Let me..."`, `"I'll..."`, `"Sure!"`, `"Looking at your..."`, `"To answer your question..."`
- **禁止事后无效复述（Forbidden Recaps）**：
  `"I've now done X, Y, and Z, which means..."`
- **禁止客套结尾（Forbidden Closers）**：
  `"Let me know if you need anything else"`, `"Hope this helps"`, `"Happy to clarify"`, `"Feel free to ask."`

### 2.2 发送前强制自检过滤器（Pre-send Check）
在 `SKILL.md:130-143`，定义了输出生成后的五项“删减过滤器”：
```markdown
Before sending, delete:
1. The first sentence if it announces what you are about to do. (删掉预告要做什么的废话)
2. The last sentence if it asks "anything else?" or recaps what just happened. (删掉客套结尾)
3. Any "by the way" sidebar. (删掉顺便发散的题外话)
4. Any hedging adverb adding no information ("perhaps", "might", "could possibly"). (删掉无信息量的推测副词)
5. Any idiom or figurative phrase ("circle back", "get the ball rolling"). Replace with the literal action. (删掉行业黑话，换成字面动作)

终极检验：
如果读者只看【第一行】和【最后一行】，他们是否清楚知道：
(a) 下一步具体要做什么？
(b) 刚才具体发生了什么？
如果满足，才允许发送！
```

### 2.3 异常熔断保护：何时允许破例？
在 `SKILL.md:119-129` 中，它并不是死板的字数限制，而是配有 6 大安全破例条款：
1. **用户显式要求解释（Explain / Walk me through）**：放开篇幅，但仍严禁开场白和客套结尾，使用多级标题方便回溯；
2. **破坏性高危动作（Destructive Action）**：涉及 `rm -rf`、强制推送、修改库表结构时，**安全审查优先于简洁性**，必须停下确认；
3. **调试死循环（Debug Spiral）**：若连续 3 轮报错相同，严禁盲目尝试改代码，必须跳出循环反问底层假设；
4. **底层契约冲突时宿主优先**：若与 Agent Harness 的系统安全规则冲突，系统规则绝对优先。

---

## 3. 对我们系统的复用方案

| 偷师模块 | 对应规范文件 | 拟引入到本项目的哪部分 | 收益与解决的痛点 |
|---|---|---|---|
| **Pre-send Check 过滤器** | `SKILL.md:130-143` | 工作台 Agent 系统级 Prompt | 强制 Agent 输出结论先行，消灭客套废话，平均单轮节省 15%~25% Token |
| **Debug Spiral 熔断门禁** | `SKILL.md:125-126` | 自动化测试与修复循环 | 连续重试 3 次未果强制挂起求助人类，杜绝 Token 额度在盲目重试中烧光 |
| **行动先行（Action First）语法** | `SKILL.md:33-41` | 两台交接文档与 CLI 输出模板 | 将多步复杂指导压缩为“带行号的精确代码变更 + 单一验证命令” |
