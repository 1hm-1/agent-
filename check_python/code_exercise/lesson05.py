# 1
for i in range(1,11):
    print(i)

# 2
a = [1,2,3]
total =0
for i in a:
    total = total + i
print(total)

# 3
texts = ["hello", "", "python", "", "agent"]
for text in texts:
    if text == "":
        continue
    else:
        print(text)

# 4
info = {
    "name": "Alice",
    "age": 18,
    "city": "Sydney"
}
for key, value in info.items():
    print(key)
    print(value)

# 5
while True:
    i = input()
    if i == "exit":
        break
    print(i)

# 6
messages = [
    {"role": "system", "content": "You are helpful."},
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好"}
]
for msg in messages:
    print(msg["role"], msg["content"])

