# 第 6 讲：函数基础

## 这一讲的目标

学完这一讲，你应该能做到：

- 理解为什么要使用函数
- 会定义和调用函数
- 理解参数和返回值
- 知道默认参数的作用
- 初步理解位置参数和关键字参数

函数是从“能写代码”走向“能组织代码”的第一步。后面做 Agent 时，很多逻辑都应该拆成函数，而不是全部堆在一个文件里。

---

## 1. 为什么需要函数？

先看一个没有函数的例子：

```python
name = "Alice"
print("你好，" + name)

name = "Bob"
print("你好，" + name)
```

这段代码能运行，但你会发现：

- 重复逻辑很多
- 一旦问候格式要改，需要改很多处

函数的作用，就是把重复逻辑封装起来。

---

## 2. 最简单的函数

定义函数使用 `def`：

```python
def say_hello():
    print("Hello")
```

调用函数：

```python
say_hello()
```

定义和调用要区分开：

- `def ...` 是定义
- `say_hello()` 是调用

---

## 3. 带参数的函数

参数可以让函数处理不同输入。

```python
def greet(name):
    print("你好，" + name)

greet("Alice")
greet("Bob")
```

这里 `name` 就是参数。

你可以把它理解成：

- 函数先留一个位置
- 调用时再把具体值传进去

---

## 4. 返回值是什么？

有些函数不只是打印结果，还要把结果“返回”出来给外部继续使用。

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

这里：

- `return` 把结果返回出去
- `result` 接住这个返回值

如果没有 `return`，函数默认返回 `None`。

---

## 5. 打印和返回的区别

这是初学者特别容易混淆的点。

```python
def add(a, b):
    print(a + b)
```

和：

```python
def add(a, b):
    return a + b
```

区别在于：

- `print()` 是直接输出到屏幕
- `return` 是把值交给外部

在真实项目里，大多数函数更应该“返回值”，而不是直接打印。

---

## 6. 默认参数

有时某些参数经常使用同一个默认值，可以这样写：

```python
def greet(name, prefix="你好"):
    print(prefix + "，" + name)

greet("Alice")
greet("Bob", "欢迎")
```

这样：

- 不传第二个参数时，用默认值
- 传了就覆盖默认值

---

## 7. 位置参数和关键字参数

例如：

```python
def introduce(name, age):
    print("我叫", name, "今年", age)
```

位置传参：

```python
introduce("Alice", 18)
```

关键字传参：

```python
introduce(name="Alice", age=18)
```

关键字传参的好处是更清楚，也不容易因为顺序错了而混乱。

---

## 8. 一个完整例子：判断是否成年

```python
def is_adult(age):
    if age >= 18:
        return True
    return False

result = is_adult(20)
print(result)
```

这里你已经把判断逻辑封装进了函数里。

这就是函数的价值：

- 主流程更清晰
- 逻辑能复用

---

## 9. 为什么函数对 Agent 开发很重要？

后面你经常会拆出这样的函数：

- `build_messages(...)`
- `call_api(...)`
- `parse_response(...)`
- `save_conversation(...)`

如果没有函数，所有逻辑都堆在一起，代码会很快变得难读、难改、难调试。

---

## 10. 常见错误

### 错误 1：定义了函数但没调用

```python
def say_hello():
    print("Hello")
```

这段代码本身不会输出任何东西，因为你只是定义了函数，还没调用。

### 错误 2：把 `print` 当成返回值

```python
def add(a, b):
    print(a + b)

result = add(2, 3)
print(result)
```

这里 `result` 会是 `None`。

### 错误 3：参数个数不匹配

```python
def add(a, b):
    return a + b

add(1)
```

会报错，因为缺少参数。

---

## 11. 这一讲你至少要完成的练习

### 练习 1：写一个问候函数

写函数 `greet(name)`，传入名字后打印问候语。

### 练习 2：写一个求和函数

写函数 `add(a, b)`，返回两个数的和。

### 练习 3：写一个判断正负的函数

写函数 `check_number(num)`：

- 大于 0 返回“正数”
- 等于 0 返回“零”
- 小于 0 返回“负数”

### 练习 4：使用默认参数

写函数 `say(message, prefix="提示")`，输出格式类似：

```text
提示: hello
```

### 练习 5：封装消息创建函数

写函数：

```python
def make_message(role, content):
    ...
```

返回：

```python
{"role": role, "content": content}
```

---

## 12. 本讲小结

这一讲最核心的是：

- 函数用来封装重复逻辑
- 参数让函数更灵活
- 返回值让函数结果能继续被使用
- 默认参数可以减少重复传值

如果你现在能自己把“创建消息字典”封装成函数，这一讲就已经掌握得不错了。

---

## 13. 下节课预告

下一讲是：

## 第 7 讲：常见内置函数与数据处理

你会开始接触：

- `len()`
- `range()`
- `enumerate()`
- `sorted()`
- 常见字符串方法
- 列表推导式入门

这些工具会明显提高你写代码的效率。

