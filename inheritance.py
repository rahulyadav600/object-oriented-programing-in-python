# there are three types of inheritance 1.single 2. multi-level 3. multiple
#single inheritance 
class car:
    color = "black"
    @staticmethod
    def start():
        print("car started ...")
        @staticmethod
        def stop():
            print("car stopped...")
class toyotacar(car):
    def __init__(self,name):
        self.name = name

car1 = toyotacar("fortuner")
car2 = toyotacar("rubicon")

print(car1.color)