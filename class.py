class Student :
# default constructor
    def __init__(self):
        print(" adding a new student in data base ")
# paramaterized constructor 
    def __init__(self,fullname):
        pass
        self.name = fullname
        print(" adding a new student in data base ")


S1 = Student("karan")
print(S1.name)


