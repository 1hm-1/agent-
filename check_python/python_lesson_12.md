# 第 12 讲：面向对象基础

## 这一讲的目标

学完这一讲，你应该能做到：

- 理解什么是类和对象
- 会写最简单的类
- 理解 `__init__` 的作用
- 会定义实例属性和方法
- 知道什么时候适合用类，什么时候函数就够了

这一讲不是让你一上来学很复杂的面向对象，而是先掌握“如何用类把相关状态和行为放在一起”。

---

## 1. 为什么会需要类？

前面你已经学过函数，函数很适合封装独立逻辑。

但如果一个东西既有“数据”，又有“行为”，类就会变得很自然。

例如一个简单 Agent 可能有：

- 名字
- system prompt
- 历史消息
- 构造消息的方法
- 发送聊天请求的方法

这些放在一起，就很适合用类表示。

---

## 2. 什么是类，什么是对象？

你可以这样理解：

- 类：蓝图
- 对象：根据蓝图创建出来的具体实例

例如：

```python
class Dog:
    pass
```

这是一个类。

创建对象：

```python
dog1 = Dog()
dog2 = Dog()
```

这里 `dog1` 和 `dog2` 都是对象。

---

## 3. 最简单的类

```python
class Person:
    def say_hello(self):
        print("你好")

p = Person()
p.say_hello()
```

这里你先知道两件事：

- 类里的函数通常叫方法
- 调用对象的方法时，写法是 `对象.方法()`

---

## 4. `__init__` 是什么？

`__init__` 是初始化方法。

当你创建对象时，它会自动执行。

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.name)
```

这里：

- `name` 是传入的参数
- `self.name` 是保存到对象里的属性

---

## 5. `self` 是什么？

入门阶段你可以先这样理解：

- `self` 代表“当前这个对象本身”

例如：

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("你好，", self.name)
```

这里 `self.name` 表示“这个对象自己的名字”。

---

## 6. 属性和方法

### 属性

对象保存的数据，比如：

- `self.name`
- `self.age`
- `self.history`

### 方法

对象能做的事，比如：

- `greet()`
- `add_message()`
- `chat()`

类的一个核心价值就是把这两者放在一起。

---

## 7. 一个完整例子：简单用户类

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我叫 {self.name}，今年 {self.age} 岁")

u = User("Alice", 18)
u.introduce()
```

这里你已经看到了：

- 创建类
- 初始化属性
- 定义方法
- 创建对象
- 调用方法

---

## 8. 什么时候适合用类？

你可以先用这个标准判断：

### 适合用类

当你有：

- 一组相关数据
- 多个会操作这些数据的方法
- 需要保存状态

例如：

- 聊天 Agent
- 用户对象
- 配置对象

### 不一定要用类

如果只是一个很小的独立功能，例如：

- 两数求和
- 清洗一个字符串
- 读取一个文件

函数通常就够了。

---

## 9. 为什么类对 Agent 开发重要？

因为后面一个最小 Agent 通常就会写成类似这样：

```python
class SimpleAgent:
    def __init__(self, system_prompt):
        self.system_prompt = system_prompt
        self.history = []

    def build_messages(self, user_input):
        ...

    def chat(self, user_input):
        ...
```

这时类就能很好地管理：

- prompt
- 历史状态
- 方法

---

## 10. 常见错误

### 错误 1：忘记写 `self`

类的方法第一个参数通常要写 `self`。

### 错误 2：把局部变量和对象属性混淆

例如：

```python
name = name
```

这不是在保存对象属性。

### 错误 3：明明只需要函数，却强行写成复杂类

入门阶段要避免过度设计。

---

## 11. 这一讲你至少要完成的练习

### 练习 1：写一个 `Student` 类

要求：

- 有 `name` 和 `age` 属性
- 有一个 `introduce()` 方法，打印自我介绍

### 练习 2：写一个 `Message` 类

要求：

- 初始化时接收 `role` 和 `content`
- 写一个方法返回字典格式：

```python
{"role": "...", "content": "..."}
```

### 练习 3：写一个 `SimpleCounter` 类

要求：

- 有一个 `count` 属性，初始值为 `0`
- 提供 `increase()` 方法，每次调用加 `1`
- 提供 `show()` 方法打印当前值

---

## 12. 本讲小结

这一讲最重要的是：

- 类是蓝图，对象是实例
- `__init__` 用来初始化对象
- `self` 表示当前对象
- 类适合管理“相关数据 + 相关行为”

---

## 13. 下节课预告

下一讲是：

## 第 13 讲：环境变量与项目配置管理

你会开始学习：

- 什么是环境变量
- 为什么 API Key 不应写死
- 如何读取配置
- 配置和代码如何分离

这会直接接到真实 API 项目的基本工程习惯。

