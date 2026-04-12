# 第 4 讲：列表、元组、集合、字典

## 这一讲的目标

学完这一讲，你应该能做到：

- 理解什么是“容器类型”
- 会使用列表保存一组有顺序的数据
- 知道元组、集合、字典分别适合什么场景
- 能对列表和字典做基础操作
- 开始理解为什么 Agent 开发里经常会出现“列表里装字典”

这一讲很重要，因为后面做 Agent 时，你最常处理的数据结构就是：

```python
[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你好"},
]
```

这本质上就是“列表 + 字典”。

---

## 1. 什么是容器类型？

前面我们学过：

- 字符串
- 整数
- 浮点数
- 布尔值

这些通常都是“单个值”。

但真实程序里，经常需要一次保存多个值，比如：

- 多个用户名
- 多条消息
- 一个用户的多项信息

这时就要用容器类型。

Python 里最常见的容器有：

- 列表 `list`
- 元组 `tuple`
- 集合 `set`
- 字典 `dict`

---

## 2. 列表：保存一组有顺序的数据

列表用方括号 `[]` 表示。

例如：

```python
names = ["Alice", "Bob", "Charlie"]
numbers = [1, 2, 3, 4]
```

列表的特点：

- 可以保存多个值
- 有顺序
- 可以重复
- 可以修改

### 2.1 访问列表元素

列表通过下标访问元素，下标从 `0` 开始。

```python
names = ["Alice", "Bob", "Charlie"]

print(names[0])
print(names[1])
```

输出：

```text
Alice
Bob
```

注意：

- 第一个元素下标是 `0`
- 第二个元素下标是 `1`

这是初学者需要适应的地方。

### 2.2 修改列表元素

```python
names = ["Alice", "Bob", "Charlie"]
names[1] = "Tom"
print(names)
```

输出：

```text
['Alice', 'Tom', 'Charlie']
```

### 2.3 往列表里添加元素

最常用的是 `append()`：

```python
names = ["Alice", "Bob"]
names.append("Charlie")
print(names)
```

输出：

```text
['Alice', 'Bob', 'Charlie']
```

### 2.4 删除列表元素

例如：

```python
names = ["Alice", "Bob", "Charlie"]
names.remove("Bob")
print(names)
```

输出：

```text
['Alice', 'Charlie']
```

### 2.5 获取列表长度

```python
names = ["Alice", "Bob", "Charlie"]
print(len(names))
```

输出：

```text
3
```

---

## 3. 列表里可以放什么？

列表里不一定只能放同一种类型。

例如：

```python
data = ["Alice", 18, True]
```

Python 允许这样做，但在真实项目里，通常更推荐让列表里的数据结构尽量一致，这样更容易处理。

例如这种更常见：

```python
scores = [85, 90, 78]
```

或者：

```python
messages = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好，请问有什么可以帮你？"}
]
```

---

## 4. 元组：有顺序，但通常不修改

元组和列表很像，但用小括号 `()` 表示。

例如：

```python
point = (10, 20)
colors = ("red", "green", "blue")
```

元组的特点：

- 有顺序
- 可以通过下标访问
- 通常不修改

例如：

```python
point = (10, 20)
print(point[0])
```

输出：

```text
10
```

### 什么时候会用元组？

当你想表达“一组固定的数据”时，可以考虑用元组，比如：

- 坐标
- 配置中的固定选项
- 不希望被改动的数据

在你当前阶段，不需要把元组学得特别深，知道它和列表的主要区别就够了。

---

## 5. 集合：无序、不重复

集合用大括号 `{}` 表示，但它和字典不同。

例如：

```python
numbers = {1, 2, 3, 3, 4}
print(numbers)
```

输出可能类似：

```text
{1, 2, 3, 4}
```

集合的特点：

- 无序
- 不重复
- 常用于去重

例如：

```python
names = ["Tom", "Tom", "Alice", "Bob", "Alice"]
unique_names = set(names)
print(unique_names)
```

这时重复项会被去掉。

### 当前阶段怎么理解集合？

你可以先把它理解为：

- “专门拿来去重”的一种结构

后面用得没有列表和字典那么频繁，但知道它的用途很有帮助。

---

## 6. 字典：用键值对保存信息

字典是 Python 里非常重要的数据结构。

字典的基本形式是：

```python
{
    "键": "值"
}
```

例如：

```python
user = {
    "name": "Alice",
    "age": 18,
    "is_student": True
}
```

这里：

- `"name"`、`"age"`、`"is_student"` 是键
- `"Alice"`、`18`、`True` 是对应的值

### 为什么字典很重要？

因为它非常适合描述“一个对象的多个属性”。

例如一个用户：

- 名字
- 年龄
- 是否登录

一个消息：

- 角色
- 内容

一个 API 返回结果：

- 状态码
- 数据
- 错误信息

---

## 7. 访问字典里的值

例如：

```python
user = {
    "name": "Alice",
    "age": 18
}

print(user["name"])
print(user["age"])
```

输出：

```text
Alice
18
```

### 修改字典里的值

```python
user = {"name": "Alice", "age": 18}
user["age"] = 19
print(user)
```

### 添加新的键值对

```python
user = {"name": "Alice"}
user["city"] = "Shanghai"
print(user)
```

### 安全读取：`get()`

有时候字典里不一定有某个键，这时可以用 `get()`：

```python
user = {"name": "Alice"}
print(user.get("age"))
```

如果没有这个键，不会立刻报错，而是返回 `None`。

也可以提供默认值：

```python
print(user.get("age", 0))
```

---

## 8. 列表和字典的区别

你可以这样记：

- 列表：通过位置取值
- 字典：通过名字取值

例如：

```python
names = ["Alice", "Bob"]
print(names[0])
```

这里是按位置取。

而：

```python
user = {"name": "Alice", "age": 18}
print(user["name"])
```

这里是按键取。

---

## 9. Agent 开发里最常见的数据结构

后面你会反复看到这样的结构：

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好，请问有什么可以帮你？"}
]
```

请你一定要看懂：

- 最外层是列表
- 列表里的每一项是字典
- 每个字典都表示一条消息

这是后面学习 Agent 时最核心的数据基础之一。

---

## 10. 一个完整例子：保存多个学生信息

```python
students = [
    {"name": "Alice", "age": 18},
    {"name": "Bob", "age": 19},
    {"name": "Tom", "age": 20}
]

print(students[0]["name"])
print(students[1]["age"])
```

这里你会看到两层访问：

- 先用列表下标取出某个学生
- 再用字典键取出学生属性

这类写法以后会非常常见。

---

## 11. 初学者常见错误

### 错误 1：列表和字典混淆

例如：

```python
names = ["Alice", "Bob"]
print(names["name"])
```

这是错的，因为列表要用数字下标，不是字符串键。

### 错误 2：访问不存在的字典键

例如：

```python
user = {"name": "Alice"}
print(user["age"])
```

这会报错，因为 `age` 不存在。

如果你不确定键是否存在，可以先用：

```python
user.get("age")
```

### 错误 3：误以为集合有顺序

集合通常不是按你写入的顺序保存的，所以不要把它当列表用。

---

## 12. 这一讲你至少要完成的练习

### 练习 1：创建一个列表

创建一个包含 5 个数字的列表，然后：

- 打印整个列表
- 打印第 1 个元素
- 打印最后一个元素

### 练习 2：修改列表

创建一个水果列表，然后：

- 添加一个水果
- 删除一个水果
- 打印修改后的列表

### 练习 3：创建一个字典

创建一个表示你自己的字典，至少包含：

- 姓名
- 年龄
- 城市

然后把这三个值都打印出来。

### 练习 4：使用 `get()`

创建一个只有 `name` 键的字典，然后尝试读取：

- `name`
- `age`

观察直接取值和 `get()` 的区别。

### 练习 5：创建消息列表

自己写出一个 `messages` 列表，至少包含：

- 一条 system 消息
- 一条 user 消息
- 一条 assistant 消息

格式类似：

```python
{"role": "...", "content": "..."}
```

这是在为后面的 Agent 开发打基础。

---

## 13. 本讲小结

这一讲最核心的是：

- 列表适合保存一组有顺序的数据
- 字典适合保存一个对象的多个属性
- 元组通常表示不想改动的一组值
- 集合常用于去重
- 后面 Agent 开发里最常见的结构是“列表里装字典”

如果你现在能自己写出一个包含多条消息的 `messages` 列表，这一讲就已经学得很到位了。

---

## 14. 下节课预告

下一讲是：

## 第 5 讲：循环与遍历

你会学到：

- `for`
- `while`
- `break`
- `continue`
- 如何遍历列表和字典

这会让你开始真正批量处理数据，而不是只处理一个值。

