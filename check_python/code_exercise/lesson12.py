class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("hello, I am " + self.name + ".I am", self.age, "years old")

class Message:
    def __init__(self, role, content):
        self.role = role
        self.content = content

    def format(self):
        return {"role": self.role, "content": self.content}
    
class SimpleCounter:
    def __init__(self, count=0):
        self.count = count
    
    def increase(self):
        self.count = self.count + 1
        return self.count
    
    def show(self):
        print(self.count)