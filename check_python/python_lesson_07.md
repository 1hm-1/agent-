# 第 7 讲：常见内置函数与数据处理

## 这一讲的目标

学完这一讲，你应该能做到：

- 会使用常见内置函数处理数据
- 理解 `len()`、`range()`、`enumerate()` 的作用
- 会用 `sorted()` 排序
- 会使用常见字符串方法
- 了解列表推导式的基本写法

这一讲的重点不是记很多 API，而是开始形成“遇到常见数据处理问题时，知道 Python 已经提供了什么工具”。

---

## 1. `len()`：获取长度

```python
names = ["Alice", "Bob", "Tom"]
print(len(names))
```

输出：

```text
3
```

`len()` 常用于：

- 列表长度
- 字符串长度
- 字典中键值对数量

---

## 2. `range()`：生成数字序列

```python
for i in range(5):
    print(i)
```

输出 `0` 到 `4`。

常见写法：

```python
range(5)
range(1, 6)
```

---

## 3. `enumerate()`：同时拿到索引和元素

```python
names = ["Alice", "Bob", "Tom"]

for index, name in enumerate(names):
    print(index, name)
```

这比自己手动维护索引更方便。

---

## 4. `sum()`、`max()`、`min()`

```python
numbers = [10, 20, 30]
print(sum(numbers))
print(max(numbers))
print(min(numbers))
```

这些函数很适合做快速统计。

---

## 5. `sorted()`：排序

```python
numbers = [3, 1, 5, 2]
print(sorted(numbers))
```

输出：

```text
[1, 2, 3, 5]
```

默认升序，也可以：

```python
print(sorted(numbers, reverse=True))
```

---

## 6. 常见字符串方法

### `strip()`

去掉首尾空白：

```python
text = "  hello  "
print(text.strip())
```

### `lower()`

转成小写：

```python
print("Hello".lower())
```

### `upper()`

转成大写：

```python
print("hello".upper())
```

### `replace()`

替换内容：

```python
print("hello world".replace("world", "python"))
```

### `split()`

按分隔符拆分：

```python
text = "a,b,c"
print(text.split(","))
```

---

## 7. `join()`：把字符串列表拼接起来

```python
words = ["I", "love", "Python"]
result = " ".join(words)
print(result)
```

输出：

```text
I love Python
```

这个在后面处理文本、消息拼接时很常见。

---

## 8. 列表推导式入门

这是 Python 很常见的一种简洁写法。

例如：

```python
numbers = [1, 2, 3, 4]
squared = [n * n for n in numbers]
print(squared)
```

输出：

```text
[1, 4, 9, 16]
```

你可以先把它理解成“更紧凑地生成新列表”的方式。

---

## 9. 一个完整例子：清洗文本列表

```python
texts = [" hello ", "", "Python ", "  agent"]
cleaned = []

for text in texts:
    text = text.strip()
    if text == "":
        continue
    cleaned.append(text)

print(cleaned)
```

这里综合使用了：

- `strip()`
- 判断空字符串
- 列表追加

这类清洗逻辑后面很常见。

---

## 10. 为什么这些工具对 Agent 开发重要？

因为你后面会经常：

- 统计消息数量
- 处理文本空格
- 排序结果
- 遍历带索引的数据
- 从列表中提取某些字段

这些都属于“基础数据处理能力”。

---

## 11. 常见错误

### 错误 1：把 `sorted()` 误以为会原地修改列表

`sorted(numbers)` 会返回一个新列表。

### 错误 2：忘记 `split()` 返回的是列表

不是字符串。

### 错误 3：列表推导式写得太复杂

入门阶段尽量只写简单版本，不要为了“短”而牺牲可读性。

---

## 12. 这一讲你至少要完成的练习

### 练习 1：统计长度

创建一个字符串和一个列表，分别使用 `len()` 输出长度。

### 练习 2：使用 `enumerate()`

遍历一个水果列表，同时打印索引和值。

### 练习 3：排序

创建一个数字列表，分别输出升序和降序排序结果。

### 练习 4：字符串处理

对一个带空格的字符串使用：

- `strip()`
- `lower()`
- `upper()`
- `replace()`

观察结果。

### 练习 5：列表推导式

给定一个数字列表，生成一个新列表，内容为每个数字的平方。

---

## 13. 本讲小结

这一讲最重要的是：

- `len()`、`range()`、`enumerate()` 是高频基础工具
- 字符串方法会在文本处理时频繁出现
- 列表推导式可以提升表达力，但要优先保证可读性

---

## 14. 下节课预告

下一讲是：

## 第 8 讲：异常处理与调试基础

你会开始学习：

- 什么是异常
- `try / except / finally`
- 常见报错类型
- 如何看懂错误信息

这是从“会写代码”走向“会解决问题”的关键一步。

