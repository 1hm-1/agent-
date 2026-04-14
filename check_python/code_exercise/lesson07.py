#1
msg = "hello "
fruits = ["apple", "banana", "grape"]
print(len(msg))
print(len(fruits))

# 2
fruits = ["apple", "banana", "grape", "blueberrys"]
for index, value in enumerate(fruits):
    print(index, value)

#3
nums = [7,5,4,2,8,6]
print(sorted(nums))
print(sorted(nums, reverse=True))

#4
message = " hELl o, worl d "
print(message.strip())
print(message.lower())
print(message.upper())
print(message.replace("worl d", "ming"))

# 5
numbers = [1, 2, 3, 4]
squared = [n * n for n in numbers]
print(squared)
