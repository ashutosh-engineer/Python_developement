#Constructor is  special method which called automatically at time of object  creation;
#--new--
#__init__

class car:
    def __new__(cls):
        print("__new__ running-Creating raw object and allocating memory")
        instance=super().__new__(cls)
        return instance

    def __init__(self):
        print("Initializing  object-Filling it with data/attributes")

car1=car()


class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle init: brand={brand}")

class Car(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand)   # calls Vehicle's __init__
        self.color = color
        print(f"Car init: color={color}")

c = Car("Toyota", "red")