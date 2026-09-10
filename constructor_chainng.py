class car:
    def __init__(self, brand):
        self.brand=brand

class vehicle(car):
    def __init__(self, brand,color):
        super().__init__(brand)
        self.color=color

S=vehicle("Toyota", "Blue")


#Destructior
class SSN:
    def __init__(self , brand, car):
        self.brand=brand
        self.car=car

    def __del__(self):
        print(f"object {self.brand} is been destroyed")

S=SSN("LL", "XX")
del S
