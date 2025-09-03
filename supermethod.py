# super method is used to access methods of the parent class 

class Car:
    def __init__(self,type):
        self.type = type

        @staticmethod
        def start():
            print("car started...")
        
        @staticmethod
        def stop():
            print("car stopped...")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name  
        super().start()
        

car1=ToyotaCar("glanza","electric")
print(car1.type)

