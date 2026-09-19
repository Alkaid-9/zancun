# L3 源码深度剖析 01 · PrimeIntellect-ai/prime-agent 递归智能体内核与持续支架

- **审查对象**：`PrimeIntellect-ai/prime-agent`
- **审计深度**：**L3 源码与安全级（Source-Code Static Audit & Mechanism Extraction）**
- **本地源码凭证**：
  - `receipts/sources/prime-agent/repl.py`（49.2 KB CPython REPL 交互内核）
  - `receipts/sources/prime-agent/harness.py`（38.8 KB 支架状态机与检索索引）
  - `receipts/sources/prime-agent/refine.py`（1.8 KB 持续微调交互契约）
  - `receipts/sources/prime-agent/goal.py`（2.0 KB 目标管理接口）
  - `receipts/sources/prime-agent/rlm_heartbeat.py`（4.3 KB 长程心跳探测）

---

## 1. 架构总览与“纸老虎”代码检验

市面大量宣传“自主多智能体（Autonomous Multi-Agent）”的开源项目，本质上只是用 `while True` 包裹静态 Prompt 拼接字符串。**Prime Agent 是真正的底层系统级突破**。

它在工程上彻底废弃了“聊天上下文即记忆”的简陋做法，提出了两大系统级支柱：
1. **RLM (Recursive Language Model) REPL 运行时**：一个常驻在后台的专用 CPython 进程，通过 stdio 管道与宿主（TypeScript Host）进行换行符分割的 JSON-RPC 双向异步通信。
2. **Continual Harness（持续进化的执行支架）**：将 Agent 的静态原则（System Prompt）与动态演进的状态（Memory / Skills / Notes）分离，支持通过 `/refine` 进行有证据约束的微调与快照秒级回滚。

```
                    ┌────────────────────────────────────────────────────────┐
                    │                 TypeScript Host (Agent UI)             │
                    └───────────────────────────┬────────────────────────────┘
                                                │ stdio JSON Lines (Protocol v3)
                                                ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        Prime Agent Python Kernel (rlm.repl)                            │
│                                                                                        │
│  ┌──────────────────────────┐   host_request   ┌─────────────────────────────────────┐ │
│  │     Active Cell Task     │ ───────────────> │  _pending_host[rid] = asyncio.Future │ │
│  │ (e.g. rlm.spawn(query))  │ <─────────────── │  _resolve_host_reply(rid, payload)  │ │
│  └──────────────────────────┘   host_reply     └─────────────────────────────────────┘ │
│               │                                                                        │
│               ▼                                                                        │
│  ┌──────────────────────────┐                  ┌─────────────────────────────────────┐ │
│  │   harness_state.json     │ <─────────────── │            refine.run()             │ │
│  │ (Memory / CJK Bigrams)   │                  │ (Turn-end hook, rebuild prompt)     │ │
│  └──────────────────────────┘                  └─────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. 核心源码逐行解剖：`repl.py`（REPL 内核与宿主通信桥）

### 2.1 JSON-RPC 协议与全局状态隔离
在 `repl.py:32-46`，定义了 REPL 的通信协议与防污染黑名单：
```python
PROTOCOL_VERSION = 3
DEFAULT_SNAPSHOT_MAX_BYTES = 256 * 1024 * 1024           # 256MB 快照上限
DEFAULT_SNAPSHOT_MAX_VARIABLE_BYTES = 16 * 1024 * 1024  # 单个变量 16MB 上限

# 核心安全黑名单：会话启动时由宿主注入，快照（Snapshot）时绝对禁止持久化
_ALWAYS_SKIP = {"rlm", "mcp", "bash", "asyncio", "In", "Out", "get_ipython", "exit", "quit", "open"}
```
**深度见解**：
很多 Agent 系统做状态保存时，直接用 `pickle.dump(locals())`，导致网络句柄、异步任务和内部模块被序列化，恢复时直接崩溃。Prime Agent 显式通过 `_ALWAYS_SKIP` 隔离了环境原生对象与用户变量。

### 2.2 跨语言双向异步调用：`host_request`
在 `repl.py:129-143`，实现了 Python 代码向 TypeScript 宿主请求子代理（Subagent）计算的 RPC 机制：
```python
async def host_request(data: dict[str, Any]) -> dict[str, Any]:
    """Send one typed request to the host and await its raw reply dict."""
    if _loop is None:
        raise RuntimeError("repl runtime is not serving")
    if _host_closed:
        raise RuntimeError("host connection closed; host_request cannot be answered")
    rid = uuid.uuid4().hex
    future: asyncio.Future[dict[str, Any]] = _loop.create_future()
    _pending_host[rid] = future
    try:
        _send({"event": "host_request", "id": rid, "data": data})
        return await future
    finally:
        _pending_host.pop(rid, None)
```
**源码机制剖析**：
1. Python 端生成一个唯一的请求 ID `rid`；
2. 在当前 asyncio 事件循环中挂起一个 `Future`；
3. 通过标准输出 `os.write(_protocol_fd, ...)` 向宿主发送单行 JSON；
4. 宿主异步调用 LLM 或运行子代理，完成后往 REPL 的标准输入回填 `{"event": "host_reply", "id": rid, "data": ...}`；
5. `_resolve_host_reply` 收到事件后，通过 `_loop.call_soon_threadsafe` 唤醒挂起的 `Future`。

**价值对齐**：
这就是为什么 Prime Agent 能做到 **`sub_result = await rlm.spawn("分析这篇论文")`**！子代理的执行结果直接作为一个结构化对象赋予 Python 内存变量，主 Agent 的聊天窗口里没有任何冗余子对话！

---

## 3. 核心源码逐行解剖：`refine.py`（持续演进与快照回滚机制）

### 3.1 杜绝运行时 Prompt 漂移的门禁
看 `refine.py:25-51` 的源码实现：
```python
async def run(
    instructions: str | None = None,
    global_: bool = False,
) -> dict[str, Any]:
    """Schedule continual harness refinement.

    Refinement never runs mid-cell: it runs when the current turn ends and
    the harness applies changes and rebuilds the system prompt, then resumes
    you automatically.
    """
    if instructions is not None and not isinstance(instructions, str):
        raise TypeError(f"instructions must be str or None, got {type(instructions).__name__}")
    payload: dict[str, Any] = {}
    if instructions is not None:
        payload["instructions"] = instructions
    if global_:
        payload["global"] = True
    return await host_request("refine.run", payload)
```
**关键工程细节（防暗坑）**：
- 注意文档里的这句硬核注释：**`Refinement never runs mid-cell: it runs when the current turn ends`**。
- 绝大多数初学者做“自进化 Agent”时，常常在代码执行中途直接去 `modify_system_prompt()`，这会导致正在执行的上下文基底断裂、KV Cache 击穿、甚至引发灾难性遗忘。
- Prime Agent 严格遵循 **原子性原则**：在 Cell 执行期间只记录微调指令（Schedule Refinement），仅在当前交互轮次（Turn）正式结束时，由外层 Harness 统一比对 Diff、构建微调快照、重编 System Prompt。

---

## 4. 核心源码逐行解剖：`harness.py`（多语言分词与高抗噪记忆索引）

很多国外开源库只支持空格分词，中文搜索直接失效。Prime Agent 在 `harness.py:43-100` 中针对东亚文字（CJK）做了底层字符级与二元语法（Bigram）切分优化：

```python
_CJK_TERM_CHARS = re.compile(
    r"[぀-ヿ㐀-䶿一-鿿豈-﫿가-힯"
    r"\U00020000-\U0002a6df\U0002a700-\U0002b73f\U0002b740-\U0002b81f"
    r"\U0002b820-\U0002ceaf\U0002ceb0-\U0002ebef\U0002ebf0-\U0002ee5f"
    r"\U0002f800-\U0002fa1f\U00030000-\U0003134f\U00031350-\U000323af"
    r"\U000323b0-\U0003347f]"
)

def _harness_query_terms(query: str) -> list[str]:
    terms: list[str] = []
    seen: set[str] = set()
    for run in _harness_query_runs(query.lower()):
        if _CJK_TERM_CHARS.search(run):
            # Bigrams keep whitespace-free CJK findable without single
            # characters matching too loosely.
            candidates = [run[i : i + 2] for i in range(len(run) - 1)] or [run]
        elif run.isascii():
            # 英文处理逻辑
            ...
```
**实现机制解读**：
中文没有空格，如果直接按单字索引匹配度太低，如果按长词匹配又搜不准。Prime Agent 将 `修复登录故障` 切分为 `修复`、`复登`、`登录`、`录故`、`故障` 的滑动 Bigram 候选词，使得输入 `修复login` 时，既能精准匹配 CJK 记忆，又不会漏词。

---

## 5. 对我们系统的复用方案（可直接偷师的代码与架构）

| 偷师模块 | 对应源码文件 | 拟引入到本项目的哪部分 | 收益与解决的痛点 |
|---|---|---|---|
| **子代理函数化抽象** | `repl.py` 中的 `host_request` / `_send` 机制 | 工作台多 Agent 协同控制面 | 彻底消灭主会话被子任务刷屏的问题，主控以函数调用方式驱动子 Agent |
| **回合尾部微调原子性** | `refine.py` 的 Turn-end 调度策略 | 两台记忆演进机制 (`/refine`) | 避免在处理长论文或代码重构中途动态篡改 System Prompt 导致上下文混乱 |
| **中英文二元分词记忆树** | `harness.py` 的 `_harness_query_terms` | 两台本地记忆检索模块 | 零依赖纯 Python 实现高命中率的中英文学术关键词检索 |
