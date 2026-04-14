# 第 14 讲：HTTP 请求与 API 调用基础

## 这一讲的目标

学完这一讲，你应该能做到：

- 理解请求和响应的基本概念
- 知道 GET 和 POST 的常见区别
- 会使用 `requests` 发送基础请求
- 知道超时、状态码和错误处理的重要性
- 理解一个最小 API 调用流程长什么样

这一讲是正式开始接近 Agent 开发实战的节点，因为调用模型 API 本质上就是一次 HTTP 请求。

---

## 1. 什么是 HTTP 请求？

你可以先把它理解成：

- 你的程序向某个服务器发出请求
- 服务器返回结果给你

例如：

- 获取天气数据
- 调用翻译服务
- 调用大模型接口

这些很多都是 HTTP 请求。

---

## 2. 请求和响应

一次请求通常包括：

- URL
- 请求方法
- 请求头
- 请求体

响应通常包括：

- 状态码
- 响应内容

入门阶段你先重点理解：

- 我发了什么
- 对方回了什么

---

## 3. GET 和 POST

### GET

通常用于“获取数据”。

### POST

通常用于“提交数据”。

在调用大模型接口时，最常见的是 POST，因为你会把消息内容作为请求体发送出去。

---

## 4. 使用 `requests`

`requests` 是 Python 里很常见的 HTTP 库。

最简单的 GET 示例：

```python
import requests

response = requests.get("https://example.com")
print(response.status_code)
print(response.text)
```

---

## 5. 发送 POST 请求

```python
import requests

payload = {
    "message": "hello"
}

response = requests.post(
    "https://example.com/api",
    json=payload,
    timeout=30
)

print(response.status_code)
print(response.text)
```

这里：

- `json=payload` 表示发送 JSON 请求体
- `timeout=30` 表示最多等 30 秒

---

## 6. 状态码是什么？

状态码表示请求结果的大致情况。

你当前阶段先记住：

- `2xx`：通常表示成功
- `4xx`：通常表示请求有问题
- `5xx`：通常表示服务器端有问题

例如：

- `200`：成功
- `404`：资源不存在
- `500`：服务器错误

---

## 7. `response.raise_for_status()`

这个方法很实用。

```python
response.raise_for_status()
```

它的作用是：

- 如果响应是错误状态码，直接抛出异常

这样你不用每次都手动判断所有状态码。

---

## 8. 解析 JSON 响应

如果服务返回的是 JSON，可以这样取：

```python
data = response.json()
print(data)
```

这通常会把响应内容转成 Python 字典或列表。

---

## 9. 一个完整例子：最小 API 调用流程

```python
import requests

payload = {
    "text": "hello"
}

try:
    response = requests.post(
        "https://example.com/api",
        json=payload,
        timeout=30
    )
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.RequestException as e:
    print("请求失败：", e)
```

这个结构很值得你记住，因为它已经很像真实项目里的最小模板了。

---

## 10. 为什么超时很重要？

如果你不设置超时，有时请求可能会一直卡着。

这在真实项目里体验很差，也很难排查。

所以：

- 网络请求一般建议显式设置 `timeout`

---

## 11. 为什么这对 Agent 开发重要？

因为你后面做的这些事情，本质上都和 API 调用有关：

- 请求模型生成回复
- 请求 embedding 接口
- 请求工具服务
- 请求外部数据源

所以 HTTP 基础不是“可选项”，而是核心基础之一。

---

## 12. 常见错误

### 错误 1：忘记处理异常

网络请求失败是常态，不是意外。

### 错误 2：不设置超时

可能导致程序一直卡住。

### 错误 3：以为返回的一定是成功

真实接口常常会失败或返回错误结构。

---

## 13. 这一讲你至少要完成的练习

### 练习 1：写一个最小 POST 请求函数

写函数 `call_api(payload)`，要求：

- 使用 `requests.post`
- 使用 JSON 请求体
- 设置超时
- 打印状态码

URL 可以先写成示例地址，不要求真实可用。

### 练习 2：模拟错误处理

给请求逻辑加上 `try / except`，当请求失败时打印友好的错误信息。

### 练习 3：设计一个模型请求体

自己写一个字典，模拟模型调用参数，至少包含：

- `model`
- `messages`

其中 `messages` 至少包含两条消息。

---

## 14. 本讲小结

这一讲最重要的是：

- HTTP 请求是程序和外部服务通信的方式
- POST 常用于提交数据
- `requests` 是常见工具
- `timeout`、状态码、异常处理都很重要

---

## 15. 下节课预告

下一讲是：

## 第 15 讲：消息结构、上下文与简单聊天程序

你会开始学习：

- 如何构造 `messages`
- 如何维护历史上下文
- 一个最小聊天循环如何组织

这会直接进入 Agent 形态。

