class car:
    @staticmethod
    def start():
        print("car started ...")
        @staticmethod
        def stop():
            print("car stopped...")
class toyotacar(car):
    def __init__(self,brand):
        self.brand = brand

class fortuner(toyotacar):
    def __init__(self,type):
        self.type = type

car1 = fortuner("diesel")
car1.start()


