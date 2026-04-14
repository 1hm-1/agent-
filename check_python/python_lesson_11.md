# 第 11 讲：JSON、配置与数据交换

## 这一讲的目标

学完这一讲，你应该能做到：

- 理解 JSON 是什么
- 知道 Python 字典和 JSON 的关系
- 会使用 `json.load()`、`json.dump()`
- 会把简单配置保存到 JSON 文件
- 理解为什么 API 和 Agent 项目里会大量使用 JSON

这一讲是从“会处理 Python 数据”走向“会和外部系统交换数据”的关键一步。

---

## 1. JSON 是什么？

JSON 是一种很常见的数据交换格式。

你可以先把它理解成：

- 一种文本格式
- 适合保存结构化数据
- 很适合程序之间传递数据

例如：

```json
{
  "name": "Alice",
  "age": 18,
  "is_student": true
}
```

很多 API 返回的内容，本质上就是 JSON。

---

## 2. JSON 和 Python 字典的关系

它们看起来很像，但不是同一个东西。

### Python 字典

```python
user = {
    "name": "Alice",
    "age": 18,
    "is_student": True
}
```

### JSON

```json
{
  "name": "Alice",
  "age": 18,
  "is_student": true
}
```

你可以这样记：

- Python 字典：Python 程序里的数据
- JSON：一种文本格式

---

## 3. 为什么 JSON 很重要？

因为后面你会经常遇到这些场景：

- API 返回 JSON
- 配置文件写成 JSON
- 保存对话历史为 JSON
- 读写结构化数据

这也是 Agent 开发里的高频基础。

---

## 4. `json.dump()`：把 Python 数据写入 JSON 文件

```python
import json

data = {
    "model": "gpt-4.1",
    "temperature": 0.7,
    "debug": True
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

这里重点看两个参数：

- `ensure_ascii=False`：让中文正常保存
- `indent=2`：让文件更好读

---

## 5. `json.load()`：从 JSON 文件读取数据

```python
import json

with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
print(data["model"])
```

读回来后，`data` 在 Python 里通常会变成字典或列表。

---

## 6. `json.dumps()` 和 `json.loads()`

它们和 `dump/load` 很像，但处理的是“字符串”而不是文件。

### `json.dumps()`

把 Python 数据转成 JSON 字符串：

```python
import json

data = {"name": "Alice", "age": 18}
text = json.dumps(data, ensure_ascii=False)
print(text)
```

### `json.loads()`

把 JSON 字符串转回 Python 数据：

```python
import json

text = '{"name": "Alice", "age": 18}'
data = json.loads(text)
print(data)
```

---

## 7. 一个完整例子：保存配置并读取回来

```python
import json

config = {
    "model": "gpt-4.1",
    "temperature": 0.5,
    "max_retries": 3
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

with open("config.json", "r", encoding="utf-8") as f:
    loaded_config = json.load(f)

print(loaded_config)
print(loaded_config["model"])
```

这就是最基础的配置读写流程。

---

## 8. JSON 常见数据类型

JSON 里常见的结构有：

- 对象：类似 Python 字典
- 数组：类似 Python 列表
- 字符串
- 数字
- 布尔值
- `null`

在 Python 里通常对应：

- `dict`
- `list`
- `str`
- `int / float`
- `True / False`
- `None`

---

## 9. 为什么 `ensure_ascii=False` 很重要？

例如：

```python
data = {"message": "你好"}
```

如果不加 `ensure_ascii=False`，保存后的 JSON 里中文可能会变成转义形式，看起来不直观。

加上之后更适合你当前阶段阅读和调试。

---

## 10. 常见错误

### 错误 1：把 JSON 当字典直接写

JSON 文件本身是文本，不是 Python 代码。

### 错误 2：忘记导入 `json`

需要先：

```python
import json
```

### 错误 3：混淆 `load` 和 `loads`

你可以这样记：

- `load`：从文件读
- `loads`：从字符串读

---

## 11. 为什么这对 Agent 开发重要？

因为后面你会频繁处理：

- 模型返回的 JSON
- tool calling 的参数
- 配置文件
- 历史消息的持久化

这已经是非常接近真实项目的基础能力了。

---

## 12. 这一讲你至少要完成的练习

### 练习 1：保存一个配置文件

创建一个字典，包含：

- `model`
- `temperature`
- `debug`

把它保存成 `config.json`。

### 练习 2：读取配置文件

把刚才保存的 `config.json` 读回来，并打印其中两个字段。

### 练习 3：保存消息列表

创建一个 `messages` 列表，里面放 2 到 3 条消息字典，然后把它保存成 JSON 文件。

### 练习 4：处理 JSON 字符串

自己写一个 JSON 字符串，使用 `json.loads()` 转成 Python 数据，再取出其中的一个字段。

---

## 13. 本讲小结

这一讲最重要的是：

- JSON 是结构化数据交换格式
- Python 字典和 JSON 看起来像，但不是同一种东西
- `json.dump/load` 处理文件
- `json.dumps/loads` 处理字符串
- 配置和 API 数据都经常使用 JSON

---

## 14. 下节课预告

下一讲是：

## 第 12 讲：面向对象基础

你会开始接触：

- 类与对象
- `__init__`
- 实例属性和方法
- 什么时候适合用类

这会为后面的 `SimpleAgent` 类做准备。

