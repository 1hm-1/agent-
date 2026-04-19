# 第 17 讲：`re` 正则表达式基础与返回解析器入门

## 这一讲的目标

学完这一讲，你应该能做到：

- 理解什么是正则表达式
- 知道为什么返回解析器常依赖 `re`
- 会使用 `re.search()`、`re.findall()`、`re.match()`
- 理解分组、转义、量词这些最常见概念
- 能写一个最小版的 `Action: Search[xxx]` 解析器

这一讲不追求把正则一次学透，而是让你先能读懂和改动 Agent 项目里最常见的解析代码。

---

## 1. 什么是 `re`？

`re` 是 Python 标准库里的正则表达式模块。

最常见的导入方式是：

```python
import re
```

它主要用于：

- 在字符串里查找特定模式
- 提取某一部分内容
- 判断文本是否符合某种格式
- 对文本做替换

---

## 2. 为什么返回解析器常依赖 `re`？

因为大模型的输出虽然是文本，但我们常常希望它遵守某种固定格式。

例如 ReAct 风格输出：

```text
Thought: 我需要先搜索一下
Action: Search[英伟达最新的 GPU 型号]
```

这时程序需要做的不是“看懂全文”，而是：

- 找到 `Action:` 这一行
- 识别工具名 `Search`
- 提取工具输入 `英伟达最新的 GPU 型号`

这种“从一段文本里按模式提取信息”的任务，正则表达式非常适合。

---

## 3. 一个最简单的匹配例子

```python
import re

text = "我的电话是 12345"
result = re.search(r"\d+", text)

if result:
    print(result.group())
```

这里：

- `\d+` 表示“一个或多个数字”
- `re.search()` 表示在整段字符串里寻找第一个匹配
- `result.group()` 表示取出匹配到的文本

输出：

```python
12345
```

---

## 4. `r"..."` 是什么？

正则里经常会看到：

```python
r"\d+"
```

前面的 `r` 表示原始字符串。

这样写的好处是：

- 反斜杠不用再额外转义

例如正则里的 `\d` 表示数字。

如果不用原始字符串，你通常要写成：

```python
"\\d+"
```

所以实际开发里，正则几乎都推荐写成：

```python
r"\d+"
```

---

## 5. `re.search()`、`re.match()`、`re.findall()` 的区别

### `re.search()`

在整个字符串中查找第一个匹配。

```python
import re

text = "abc 123 xyz"
result = re.search(r"\d+", text)
print(result.group())
```

输出：

```python
123
```

### `re.match()`

只从字符串开头开始匹配。

```python
import re

text = "abc 123"
result = re.match(r"\d+", text)
print(result)
```

这里结果是 `None`，因为开头不是数字。

### `re.findall()`

找出所有匹配项，返回列表。

```python
import re

text = "价格是 12 元，折扣后是 9 元"
result = re.findall(r"\d+", text)
print(result)
```

输出：

```python
['12', '9']
```

---

## 6. 最常见的几个正则符号

### `\d`

匹配一个数字。

```python
r"\d"
```

### `\w`

匹配字母、数字、下划线。

```python
r"\w+"
```

### `.`

匹配任意单个字符，但通常不包括换行。

```python
r"a.c"
```

可以匹配：

- `abc`
- `a1c`

### `+`

表示前面的模式出现一次或多次。

```python
r"\d+"
```

### `*`

表示前面的模式出现零次或多次。

```python
r"\d*"
```

### `?`

表示前面的模式出现零次或一次。

```python
r"\d?"
```

---

## 7. 什么是分组？

分组就是用括号把你关心的部分圈出来，方便后面单独提取。

例如：

```python
import re

text = "Action: Search[北京天气]"
result = re.search(r"Action:\s*(\w+)\[(.*)\]", text)

if result:
    print(result.group(1))
    print(result.group(2))
```

输出：

```python
Search
北京天气
```

这里：

- `group(1)` 是第一个括号匹配到的内容
- `group(2)` 是第二个括号匹配到的内容

这就是返回解析器最常见的用法之一。

---

## 8. `\s*` 是什么意思？

```python
\s
```

表示空白字符，例如：

- 空格
- 制表符
- 换行

```python
\s*
```

表示“零个或多个空白字符”。

所以：

```python
r"Action:\s*(\w+)\[(.*)\]"
```

可以同时匹配：

```text
Action: Search[北京天气]
```

也可以匹配：

```text
Action:    Search[北京天气]
```

---

## 9. 为什么方括号前面有时要加反斜杠？

因为在正则里，`[` 和 `]` 本身也有特殊含义。

如果你想匹配字面量的方括号，就要写成：

```python
\[
\]
```

例如：

```python
r"Search\[(.*)\]"
```

表示匹配：

```text
Search[北京天气]
```

而不是把 `[` 当成正则语法的一部分。

---

## 10. 一个最小版 Action 解析器

```python
import re

def parse_action(text):
    pattern = r"Action:\s*(\w+)\[(.*)\]"
    result = re.search(pattern, text)

    if not result:
        return None

    tool_name = result.group(1)
    tool_input = result.group(2)
    return tool_name, tool_input


text = "Thought: 我需要先搜索\nAction: Search[英伟达最新的 GPU 型号]"
print(parse_action(text))
```

输出：

```python
('Search', '英伟达最新的 GPU 型号')
```

这个例子已经非常接近 ReAct 项目里的真实解析逻辑了。

---

## 11. 一个更完整的解析思路

很多返回解析器不只要识别工具调用，还要识别最终答案。

例如模型可能返回：

```text
Thought: 我已经拿到答案
Action: Finish[目前最新型号是某某]
```

这时你可以继续用类似思路：

```python
import re

def parse_response(text):
    result = re.search(r"Action:\s*(\w+)\[(.*)\]", text)
    if not result:
        return None

    action_name = result.group(1)
    action_input = result.group(2)
    return action_name, action_input
```

如果：

- `action_name == "Search"`，就调用工具
- `action_name == "Finish"`，就结束流程并返回答案

---

## 12. 为什么有时正则会“贪婪”？

看这个例子：

```python
import re

text = "Action: Search[北京][额外内容]"
result = re.search(r"Action:\s*(\w+)\[(.*)\]", text)
print(result.group(2))
```

这里 `.*` 是贪婪匹配，意思是：

- 尽量多吃字符

所以它可能会一直匹配到最后一个 `]`。

如果你只想更克制地匹配，可以使用非贪婪写法：

```python
r"Action:\s*(\w+)\[(.*?)\]"
```

这里的 `.*?` 表示：

- 尽量少匹配

在很多解析器里，这个区别很重要。

---

## 13. `group()`、`groups()` 是什么？

### `group()`

取完整匹配结果。

```python
import re

text = "Action: Search[北京天气]"
result = re.search(r"Action:\s*(\w+)\[(.*?)\]", text)

print(result.group())
```

输出是整段匹配内容。

### `groups()`

一次性返回所有分组内容。

```python
print(result.groups())
```

输出类似：

```python
('Search', '北京天气')
```

---

## 14. `re.sub()` 是什么？

它用于替换文本。

```python
import re

text = "价格是 100 元"
new_text = re.sub(r"\d+", "XXX", text)
print(new_text)
```

输出：

```python
价格是 XXX 元
```

返回解析器里有时会先用 `sub()` 清洗空白、换行或无关符号。

---

## 15. 返回解析器里最常见的错误

### 错误 1：把正则写得过死

例如只允许一个空格，但模型输出有两个空格，就匹配失败。

这时通常要考虑：

- `\s*`
- `\s+`

### 错误 2：忘记判空

```python
result = re.search(...)
print(result.group(1))
```

如果没匹配到，`result` 是 `None`，会直接报错。

所以要先判断：

```python
if result:
    ...
```

### 错误 3：没有处理贪婪匹配

`.*` 很方便，但有时会吃太多。

### 错误 4：以为正则能解决所有解析问题

如果输出结构非常复杂，正则就会越来越难维护。

这时可以考虑：

- 让模型输出 JSON
- 分多步解析
- 限制格式更严格

---

## 16. 一个贴近 Agent 的小练习

请自己尝试解析下面这段文本：

```text
Thought: 我需要查一下实时信息
Action: Search[今天上海天气]
```

要求：

- 提取 `Search`
- 提取 `今天上海天气`

你可以使用：

```python
re.search()
group(1)
group(2)
```

---

## 17. 当前阶段你至少要掌握到什么程度？

你现在不需要背下所有正则语法。

更现实的目标是：

- 看懂 `re.search()` 在做什么
- 看懂 `(\w+)` 和 `(.*)` 这样的分组
- 能理解为什么解析器会写 `if result:`
- 能自己改一个简单的 `Action: Search[...]` 匹配规则

做到这些，就已经足够支撑你继续学习 ReAct 和返回解析器了。

