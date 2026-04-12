# 第 5 讲：循环与遍历

## 这一讲的目标

学完这一讲，你应该能做到：

- 理解为什么程序需要循环
- 会使用 `for` 循环遍历数据
- 会使用 `while` 循环处理重复逻辑
- 理解 `break` 和 `continue`
- 能遍历列表和字典
- 能写出基础的批量处理程序

这一讲非常重要，因为一旦你开始处理“很多条消息”“很多个文件”“很多个结果”，循环就会变成你的日常工具。

---

## 1. 为什么需要循环？

如果没有循环，很多事情会很麻烦。

例如你想打印 5 次“Hello”。

不用循环的话只能写：

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

这显然很笨重。

更现实的情况是：

- 遍历一个用户名列表
- 逐条处理消息记录
- 对多个 API 返回结果做检查

这些都需要循环。

---

## 2. `for` 循环：遍历一组数据

最常见的循环是 `for`。

例如：

```python
names = ["Alice", "Bob", "Tom"]

for name in names:
    print(name)
```

输出：

```text
Alice
Bob
Tom
```

这里的意思是：

- 从 `names` 列表里
- 每次取出一个元素
- 放到变量 `name` 里
- 执行缩进内的代码

### 结构拆解

```python
for 变量 in 可遍历对象:
    要重复执行的代码
```

---

## 3. `for` 循环是怎么工作的？

例如：

```python
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

执行过程可以理解为：

1. 先取出 `10`，赋值给 `num`
2. 执行 `print(num)`
3. 再取出 `20`
4. 再执行一次
5. 再取出 `30`
6. 再执行一次

所以 `for` 特别适合做“遍历”。

---

## 4. 使用 `range()` 生成序列

如果你只是想重复执行若干次，可以配合 `range()`。

例如：

```python
for i in range(5):
    print(i)
```

输出：

```text
0
1
2
3
4
```

注意：

- `range(5)` 不包括 `5`
- 它会生成从 `0` 到 `4`

### 如果你想打印 1 到 5

```python
for i in range(1, 6):
    print(i)
```

输出：

```text
1
2
3
4
5
```

---

## 5. `while` 循环：条件满足就一直执行

`while` 的特点是：

- 只要条件为真，就一直重复

例如：

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

输出：

```text
1
2
3
4
5
```

这里一定要注意：

- `count = count + 1` 很重要
- 如果你忘了更新变量，循环可能永远停不下来

---

## 6. `for` 和 `while` 的区别

你可以先这样理解：

- `for`：适合遍历一个已有的数据集合
- `while`：适合在某个条件成立时持续执行

例如：

- 遍历一个列表，优先用 `for`
- 一直让用户输入，直到输入 `exit`，更适合 `while`

---

## 7. `break`：提前结束循环

例如：

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

输出：

```text
0
1
2
3
4
```

因为当 `i == 5` 时，循环直接结束了。

### `break` 适合什么场景？

- 找到目标后就停止
- 用户输入了退出命令
- 某个错误发生后不再继续处理

---

## 8. `continue`：跳过本次，继续下一次

例如：

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

输出：

```text
0
1
3
4
```

这里：

- 当 `i == 2` 时，不执行这次后面的 `print`
- 直接进入下一轮循环

### `continue` 适合什么场景？

- 跳过无效数据
- 跳过空字符串
- 跳过某些不满足处理条件的项

---

## 9. 遍历列表

这是最常见的写法之一。

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print("水果是：", fruit)
```

### 配合条件判断

```python
messages = ["hi", "", "hello", "bye"]

for msg in messages:
    if msg == "":
        continue
    print(msg)
```

这段代码会跳过空字符串。

这类逻辑后面处理消息列表时非常常见。

---

## 10. 遍历字典

字典也可以遍历。

例如：

```python
user = {
    "name": "Alice",
    "age": 18,
    "city": "Shanghai"
}

for key in user:
    print(key)
```

这会遍历字典的键。

### 同时拿到键和值

更常见的是：

```python
for key, value in user.items():
    print(key, value)
```

输出类似：

```text
name Alice
age 18
city Shanghai
```

---

## 11. 遍历“列表里装字典”

这类结构你后面会非常常见。

例如：

```python
messages = [
    {"role": "system", "content": "You are helpful."},
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好"}
]
```

遍历方式：

```python
for message in messages:
    print(message["role"], message["content"])
```

这就是后面处理聊天历史的基础。

---

## 12. 一个完整例子：统计总分

```python
scores = [80, 90, 75, 88]
total = 0

for score in scores:
    total = total + score

print("总分是：", total)
```

这段代码做了什么：

1. 先把总分初始化为 `0`
2. 每遍历到一个成绩，就加到 `total` 里
3. 最后输出结果

这个思路在以后会频繁出现。

---

## 13. 一个完整例子：命令行退出循环

```python
while True:
    text = input("请输入内容，输入 exit 退出：")

    if text == "exit":
        print("程序结束")
        break

    print("你输入的是：", text)
```

这是一个很经典的交互式循环：

- 一直等待用户输入
- 如果输入 `exit`，就停止
- 否则继续处理

后面写最小聊天程序时，基本就是这个模式。

---

## 14. 常见错误

### 错误 1：`while` 忘记更新变量

例如：

```python
count = 1

while count <= 5:
    print(count)
```

这会陷入死循环，因为 `count` 一直没有变化。

### 错误 2：遍历时把列表和字典搞混

例如：

```python
names = ["Alice", "Bob"]

for name in names:
    print(name["first"])
```

这里 `name` 是字符串，不是字典，所以会报错。

### 错误 3：缩进不正确

循环里的代码必须缩进，否则不会属于循环体。

### 错误 4：不理解 `break` 和 `continue`

你可以这样记：

- `break`：整个循环停了
- `continue`：这一次跳过，下一次继续

---

## 15. 为什么循环对 Agent 开发特别重要？

因为你后面会不断做这些事：

- 遍历消息历史
- 遍历工具调用结果
- 遍历文件列表
- 重试请求
- 一轮一轮执行 Agent 流程

所以循环是最常用的程序结构之一。

---

## 16. 这一讲你至少要完成的练习

### 练习 1：打印 1 到 10

使用 `for` 循环打印 `1` 到 `10`。

### 练习 2：计算列表总和

给定一个数字列表，使用循环求和并打印结果。

### 练习 3：跳过空字符串

给定：

```python
texts = ["hello", "", "python", "", "agent"]
```

使用循环打印非空字符串。

### 练习 4：遍历字典

创建一个包含姓名、年龄、城市的字典，使用循环打印所有键和值。

### 练习 5：实现一个简单输入循环

不断读取用户输入：

- 如果输入 `exit`，程序结束
- 否则打印用户输入内容

### 练习 6：遍历消息列表

创建一个 `messages` 列表，每项是一个字典，包含：

- `role`
- `content`

然后使用循环把每条消息打印出来。

---

## 17. 本讲小结

这一讲最重要的是：

- `for` 适合遍历数据
- `while` 适合按条件重复执行
- `break` 用来提前结束循环
- `continue` 用来跳过本轮
- 列表和字典都可以遍历
- “遍历列表中的字典”是后面 Agent 开发里的高频操作

如果你现在能自己写出一个“循环读取输入，直到用户输入 exit 才退出”的小程序，这一讲就已经掌握得不错了。

---

## 18. 下节课预告

下一讲是：

## 第 6 讲：函数基础

你会开始学到：

- 为什么要把代码封装成函数
- 参数和返回值是什么
- 默认参数
- 位置参数与关键字参数

这是从“会写代码”走向“会组织代码”的第一步。

