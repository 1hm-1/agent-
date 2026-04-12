# Python 能力自测：我是否已经具备学习 Agent 开发的基础？

这份题目不是考试，更像一份定位清单。

目标很简单：帮助你判断自己是否已经具备学习 Agent 开发的 Python 基础，以及还差在哪些点。

## 怎么使用这份题

建议你按下面的方式做：

1. 先独立完成，不查答案。
2. 能运行的题尽量自己写成 `.py` 文件执行。
3. 做完后按文末标准给自己打分。
4. 不会的题不要只看结果，要确认自己是卡在：
   - Python 语法
   - 标准库使用
   - 代码组织能力
   - 调试能力
   - 对 API / 异步 / 工程化的陌生

---

## 你学习 Agent 开发时，Python 需要掌握到什么程度？

不需要非常强的算法竞赛能力，但通常需要这些能力：

- 能读懂并改写已有 Python 代码
- 能写函数、类、模块
- 能处理 JSON、文件、异常
- 能调用 HTTP API
- 能理解异步 `async/await` 的基本用法
- 能写出结构清晰、便于调试的小项目

如果下面大部分题你都能独立完成，你的 Python 基础通常已经足够开始学 Agent 开发。

---

## 第一部分：基础语法与数据处理

### 题 1：清洗消息列表

给定一个消息列表：

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": ""},
    {"role": "user", "content": "Tell me a joke"},
    {"role": "assistant", "content": None},
]
```

写一个函数 `clean_messages(messages)`，返回一个新列表，要求：

- 只保留 `content` 是非空字符串的项
- 保持原顺序不变
- 不修改原列表

请额外说明：

- 你为什么没有直接在原列表上删除元素？

---

### 题 2：统计 token 近似值

写一个函数 `estimate_tokens(text)`，规则如下：

- 英文按空格拆分，单词数视为 token 数
- 中文按字符数近似视为 token 数
- 如果中英混合，你可以自行设计一个简单合理的估算方法

要求：

- 给出你的实现
- 写 3 个测试样例
- 简要说明这种估算为什么不精确

---

### 题 3：按 role 分组

给定：

```python
messages = [
    {"role": "user", "content": "A"},
    {"role": "assistant", "content": "B"},
    {"role": "user", "content": "C"},
    {"role": "tool", "content": "D"},
]
```

输出一个字典，格式类似：

```python
{
    "user": ["A", "C"],
    "assistant": ["B"],
    "tool": ["D"]
}
```

要求：

- 不要写死 role 名称
- 如果某项缺少 `role` 或 `content`，请安全跳过

---

## 第二部分：函数、异常与可维护性

### 题 4：重试函数

实现函数：

```python
def retry(func, max_retries=3):
    ...
```

要求：

- 调用 `func()`
- 如果抛出异常，则最多重试 `max_retries` 次
- 最终成功则返回结果
- 如果最终仍失败，则把最后一次异常继续抛出

思考题：

- 为什么在 Agent 调用外部 API 时经常需要重试？
- 哪些错误适合重试，哪些错误不适合？

---

### 题 5：解析模型响应

写函数 `parse_response(data)`，其中 `data` 是一个 Python 字典。

你要从中读取：

```python
data["choices"][0]["message"]["content"]
```

要求：

- 如果结构正确，返回字符串内容
- 如果缺字段、类型不对、列表为空，不要报原始异常
- 改为抛出你自己定义的异常，例如 `ResponseFormatError`

这题主要考察：

- `try/except`
- 自定义异常
- 对外提供稳定接口

---

### 题 6：重构坏代码

下面这段代码可读性很差，请重构：

```python
def run(x):
    a = []
    for i in x:
        if "content" in i:
            if i["content"]:
                if len(i["content"]) < 100:
                    a.append(i["content"])
    return ",".join(a)
```

要求：

- 改成更清晰的版本
- 命名更合理
- 可适当拆函数
- 保持原有行为基本一致

额外说明：

- 你为什么认为你的版本更适合真实项目维护？

---

## 第三部分：文件、JSON 与配置

### 题 7：保存对话记录

写函数 `save_conversation(messages, file_path)`：

- 把 `messages` 保存成 JSON 文件
- 使用 UTF-8
- 要保证中文不乱码
- 写入失败时进行异常处理

再写函数 `load_conversation(file_path)` 把它读回来。

要求你说明：

- `json.dump(..., ensure_ascii=False)` 的作用是什么？

---

### 题 8：读取环境变量

请写一个小示例，从环境变量中读取：

- `OPENAI_API_KEY`
- `OPENAI_BASE_URL`（可选）

要求：

- 如果 `OPENAI_API_KEY` 缺失，要给出清晰报错
- 不要把 key 打印到日志里

思考题：

- 为什么 Agent 项目里通常不把 API Key 写死在代码中？

---

### 题 9：设计配置结构

假设你要做一个简单 Agent，配置项包括：

- 模型名
- 温度
- 最大重试次数
- 是否开启调试日志

请你自己设计一种配置方式，任选其一：

- 用字典
- 用类
- 用 `dataclass`

要求：

- 给出代码
- 解释你为什么这么设计
- 说明这种方式比“到处散落硬编码”好在哪里

---

## 第四部分：HTTP API 与 Agent 基础交互

### 题 10：发送一个 POST 请求

使用 `requests` 写一个函数 `call_api(payload)`：

- 向某个 URL 发送 POST 请求
- 请求体为 JSON
- 超时时间为 30 秒
- 检查状态码
- 正常时返回 JSON 数据
- 网络失败、超时、非 2xx 响应时进行合理报错

要求：

- 不必真的请求 OpenAI
- 你可以用伪代码 URL，例如 `https://example.com/api`

思考题：

- `response.raise_for_status()` 有什么作用？

---

### 题 11：把 prompt 构造成消息格式

写函数：

```python
def build_messages(system_prompt, user_input, history=None):
    ...
```

要求返回类似：

```python
[
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
]
```

要求：

- `history` 可以为空
- 如果有 `history`，应插入到 system 和当前 user 之间
- 要避免 `history` 被原地修改

这题很接近真实 Agent 开发中的消息拼装。

---

### 题 12：实现一个最小聊天循环

写一个命令行程序：

- 启动后反复读取用户输入
- 输入 `exit` 时退出
- 每次输入后，调用一个假的 `chat(messages)` 函数
- 打印返回结果
- 维护历史上下文

这里的 `chat(messages)` 可以自己伪造，例如始终返回：

```python
"收到：" + 用户最后一句话
```

重点不在模型，而在：

- 程序流程
- 状态维护
- 函数拆分

---

## 第五部分：异步与并发基础

### 题 13：理解 async/await

请写一个异步函数：

```python
async def fake_llm_call(name, delay):
    ...
```

要求：

- 等待 `delay` 秒
- 返回字符串，例如 `"task A done"`

然后并发执行 3 个任务，并统计总耗时。

要求说明：

- 为什么并发执行的总时间通常小于串行执行？
- 这和多线程是不是一回事？

---

### 题 14：异步重试

把第 4 题的 `retry` 改造成异步版本：

```python
async def async_retry(func, max_retries=3):
    ...
```

其中 `func` 是一个异步函数。

要求：

- 正确使用 `await`
- 异常逻辑正确

这题能看出你是否真正理解异步函数调用方式。

---

## 第六部分：面向对象与代码组织

### 题 15：设计一个简单 Agent 类

请设计一个 `SimpleAgent` 类，至少包含：

- `__init__`
- `build_messages`
- `chat`

你可以假设：

- `chat` 先构造消息
- 再调用一个假的模型函数
- 最后返回结果

要求：

- 保存历史消息
- 结构清晰
- 让别人一眼能看懂类的职责

思考题：

- 哪些逻辑适合放在类里，哪些适合放在独立函数里？

---

### 题 16：给项目拆文件

如果你要把一个简单 Agent 项目拆成多个文件，你会怎么拆？

请给出一个你认可的目录结构，例如：

```text
agent_project/
  main.py
  agent.py
  config.py
  api_client.py
  utils.py
```

并解释：

- 每个文件负责什么
- 为什么这样拆
- 什么情况下拆得太早，什么情况下又拆得不够

---

## 第七部分：调试、测试与工程意识

### 题 17：定位 bug

阅读下面代码，指出至少 3 个问题：

```python
def append_message(history=[], role="user", content=""):
    history.append({"role": role, "content": content})
    return history
```

要求：

- 说明问题是什么
- 说明会导致什么后果
- 给出修复版本

---

### 题 18：写测试

为下面函数写至少 3 个测试用例：

```python
def is_valid_message(msg):
    return isinstance(msg, dict) and "role" in msg and "content" in msg
```

要求：

- 至少覆盖正常情况
- 至少覆盖异常输入
- 至少覆盖边界情况

如果你会 `pytest`，可以直接写 `pytest` 风格。

---

### 题 19：日志与排错

假设你的 Agent 偶尔会调用失败，你会记录哪些日志来帮助排错？

请至少列出 6 项，并说明哪些信息：

- 应该记录
- 不应该记录

提示：

- 请求时间
- 请求耗时
- 模型名
- 错误类型
- 用户原文
- API Key

---

### 题 20：做一个最小可运行项目

综合前面的内容，做一个最小版 Agent 项目，要求：

- 从命令行读取输入
- 用类或函数组织代码
- 使用消息列表维护上下文
- 有基本异常处理
- 有配置项
- 至少留出未来接入真实 API 的位置

你不需要真的接入大模型，但代码结构要像一个真实项目的最小雏形。

---

## 自评标准

### A 档：可以开始学 Agent 了

如果你满足下面大多数条件，Python 基础已经够用：

- 前 12 题能独立完成大部分
- 第 13 到 15 题虽然不熟，但能看懂并慢慢写出来
- 能自己调试报错，不会一报错就完全卡住
- 能读懂别人写的基础 Python 项目
- 知道 JSON、异常、函数、类、模块分别是做什么的

结论：

你已经足够开始学 Agent 开发。后面缺的更多是 API、框架和项目经验，不是 Python 门槛。

### B 档：基础基本够，但需要补几个关键点

如果你有下面情况：

- 基础语法题能做
- 一到文件、JSON、异常、requests、类，就明显吃力
- 异步完全不会
- 代码能写出来，但结构很乱

结论：

你也可以开始学 Agent，但建议先补这几个点：

- 函数与参数
- 字典、列表、JSON
- 异常处理
- 文件读写
- `requests`
- 类与模块拆分
- `async/await` 基础概念

### C 档：先补 Python，再学 Agent 会更轻松

如果你有下面情况：

- 前 6 题都很难独立完成
- 读字典和列表都经常混乱
- 函数参数、返回值、异常还不熟
- 基本调试能力较弱

结论：

先补 Python 基础更划算。否则学 Agent 时你会同时卡在：

- Python 语法
- 接口调用
- 框架概念
- 调试问题

这样学习体验会很差。

---

## 建议的最低掌握线

如果你想比较稳地开始学 Agent，建议你至少能独立完成这些题：

- 题 1
- 题 4
- 题 5
- 题 7
- 题 8
- 题 10
- 题 11
- 题 12
- 题 15
- 题 17

如果这些题你能做出 70% 以上，就已经可以开始。

---

## 下一步怎么用这份结果

你可以这样判断自己：

- 如果你能完成 70% 以上：直接开始学 Agent
- 如果你能完成 40% 到 70%：边补 Python 边学 Agent
- 如果你低于 40%：先补 2 到 3 周 Python 基础，再进入 Agent

---

## 推荐补强顺序

如果你做下来发现基础不稳，建议按这个顺序补：

1. 函数、列表、字典
2. JSON、文件读写、异常处理
3. `requests` 调 API
4. 类、模块拆分
5. `async/await`
6. 再学 Agent 框架和工具调用

---

## 给你的一个判断标准

真正决定你能不能学 Agent 的，不是“你会不会高级 Python”，而是：

- 你能不能读懂示例代码
- 你能不能改动示例代码
- 你能不能自己定位报错
- 你能不能把一个小脚本慢慢组织成小项目

如果这些方向你已经有一定能力，就可以开始。
