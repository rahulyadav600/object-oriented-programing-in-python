# used to delete object properties or object itself .
class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("shardha didi")

del s1
print(s1)