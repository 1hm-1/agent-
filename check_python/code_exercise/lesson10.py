# 1
with open("./text.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# 2
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("hello")

# 3
with open("test.txt", "a", "r", encoding="utf-8") as f:
    f.write("\nadded")
    f.write("\nanother added")
with open("test.txt", "r", encoding="utf-8") as f:
    content1 = f.read()
print(content1)

# 4
try:
    with open("1.txt", "r", encoding="utf-8") as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print("文件不存在")

# 5
with open("contrast.txt", "w", encoding="utf-8") as f:
    f.write("今天学习了python的基础知识")