# 第 15 讲：消息结构、上下文与简单聊天程序

## 这一讲的目标

学完这一讲，你应该能做到：

- 理解消息列表为什么是大模型交互的核心结构
- 会构造基础 `messages`
- 理解历史上下文的作用
- 能写一个最小聊天循环
- 开始把前面学过的函数、循环、字典、列表组合起来

这一讲是整套基础课里最接近 Agent 实战的一讲。

---

## 1. 什么是消息结构？

大模型接口里非常常见的一种结构是：

```python
[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好，请问有什么可以帮你？"}
]
```

这里：

- 最外层是列表
- 每一项是字典
- 每个字典表示一条消息

---

## 2. `role` 和 `content`

一条消息里最常见的两个字段是：

- `role`
- `content`

例如：

```python
{"role": "user", "content": "今天北京天气怎么样？"}
```

你当前阶段先理解：

- `role` 表示这条消息是谁说的
- `content` 表示消息内容

---

## 3. 为什么需要历史上下文？

如果模型只看到你最后一句输入，它就不知道前面聊了什么。

例如：

1. 用户说：“我叫小王”
2. 下一句说：“你还记得我叫什么吗？”

如果没有历史消息，模型很难答对。

所以聊天程序通常要维护一个消息列表作为上下文。

---

## 4. 构造最小消息列表

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你好"}
]
```

这已经是最基础的模型输入形式了。

---

## 5. 追加历史消息

例如：

```python
messages = []

messages.append({"role": "user", "content": "你好"})
messages.append({"role": "assistant", "content": "你好，请问有什么可以帮你？"})

print(messages)
```

这就是维护历史的最基本方式。

---

## 6. 写一个消息构造函数

```python
def make_message(role, content):
    return {"role": role, "content": content}
```

这样比每次手写字典更整洁。

---

## 7. 构造 `build_messages()` 函数

```python
def build_messages(system_prompt, user_input, history=None):
    messages = [{"role": "system", "content": system_prompt}]

    if history:
        messages.extend(history)

    messages.append({"role": "user", "content": user_input})
    return messages
```

这个函数已经非常接近真实项目了。

它做了三件事：

1. 放入 system prompt
2. 拼接历史
3. 追加当前用户输入

---

## 8. 为什么不要随便修改原始历史？

如果你直接在外部的 `history` 上反复原地修改，后面可能会出现：

- 消息重复
- 调试困难
- 状态混乱

所以在很多场景里，构造新列表会更安全。

---

## 9. 一个假的 `chat()` 函数

入门阶段我们不一定非要接入真实模型。

可以先写一个假的版本，专注于程序结构：

```python
def chat(messages):
    last_user_message = messages[-1]["content"]
    return "收到：" + last_user_message
```

这样你就能先练：

- 消息拼装
- 聊天循环
- 历史维护

---

## 10. 一个最小聊天循环

```python
history = []
system_prompt = "You are a helpful assistant."

while True:
    user_input = input("你：")

    if user_input == "exit":
        break

    messages = build_messages(system_prompt, user_input, history)
    reply = chat(messages)

    print("助手：", reply)

    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": reply})
```

这段代码已经很像一个最小版聊天程序了。

---

## 11. 为什么这对 Agent 开发重要？

因为后面更复杂的 Agent，本质上也是在做这些事：

- 组织 messages
- 保持上下文
- 调用模型
- 获取回复
- 更新历史状态

区别只是会多出：

- 工具调用
- 记忆管理
- 多轮决策

---

## 12. 常见错误

### 错误 1：忘记保存历史

这样程序每轮都像第一次对话。

### 错误 2：把 system prompt 放错位置

通常应该放在消息列表前面。

### 错误 3：直接修改传入历史导致状态混乱

初学阶段很容易出现重复追加的问题。

---

## 13. 这一讲你至少要完成的练习

### 练习 1：写一个 `make_message()` 函数

输入 `role` 和 `content`，返回消息字典。

### 练习 2：写一个 `build_messages()` 函数

要求：

- 接收 `system_prompt`
- 接收 `user_input`
- 接收可选 `history`
- 返回完整消息列表

### 练习 3：写一个最小聊天程序

要求：

- 反复读取用户输入
- 输入 `exit` 时退出
- 用一个假的 `chat()` 函数返回结果
- 维护历史上下文

---

## 14. 本讲小结

这一讲最重要的是：

- `messages` 是大模型对话的核心结构
- 上下文要靠历史消息维护
- 最小聊天程序已经能把前面很多基础知识串起来

---

## 15. 下节课预告

下一讲是：

## 第 16 讲：异步编程入门与 Agent 项目过渡

你会开始接触：

- `async` 和 `await`
- 同步与异步的区别
- 为什么 API 调用常和异步一起出现
- 一个简单 Agent 项目的代码结构

这会为你后面进入更真实的项目做过渡。

