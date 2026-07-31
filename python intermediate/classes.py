class Car:
    wheels=4
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

car1 = Car("red", "Toyota")
car2 = Car("blue", "Honda")
print(car1.wheels)

print(car1.color)   # "red"
print(car2.color)   # "blue"



#The danger of mutbale class attrribute
class Car:
    features = []   # class attribute, and it's a MUTABLE list

    def add_feature(self, feature):
        self.features.append(feature)

car1 = Car()
car2 = Car()

car1.add_feature("sunroof")

print(car1.features)   # ['sunroof']
print(car2.features)   # ['sunroof']  <-- also affected?!

#Dynamic attributes;
car1 = Car()
car1.license_plate = "MH12AB1234"   # never defined in the class, added on the fly

print(car1.license_plate)  # "MH12AB1234"


#Object lifecycle;
class Car:
    def __init__(self, color):
        self.color = color
        print(f"Car created: {color}")

car1 = Car("red")   # "Car created: red" printed -- object created
car1 = Car("blue")  # "Car created: blue" printed -- NEW object created
                     # the OLD red Car object now has 0 references (car1 no longer points to it)
                     # so it gets destroyed/deallocated automatically