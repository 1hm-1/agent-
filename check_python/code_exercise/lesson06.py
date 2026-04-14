#1
def greet(name):
    print("hello,"+name)

#2
def add(a, b):
    return a+b

#3
def check_number(num):
    if num>0:
        return "正数"
    elif num < 0:
        return "负数"
    else:
        return "零"

#4 
def say(msg, prefix="提示"):
    print(prefix+":"+msg)
say("hello")

#5
def make_message(role, content):
    return {"role": role, "content": content}