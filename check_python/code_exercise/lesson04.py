# 1
list1 = [1,2,3,4,5]
print(list1[0])
print(list1[-1])
# 2
fruit = ['apple', 'orange']
fruit.append('grape')
fruit.remove('apple')
print(fruit)

# 3
me = {
    "name": "hm",
    "age" : 21,
    "city": "Mianyang"
}
print(me["name"])
print(me["age"])
print(me["city"])

# 4
temp = {
    "name": "Lisa"
}
print(temp.get("name"))
print(temp.get("age"))

# 5
msg = [
    {"role": "system", "content": "00"},
    {"role": "user", "content": "01"},
    {"role": "assistant", "content": "11"},
]