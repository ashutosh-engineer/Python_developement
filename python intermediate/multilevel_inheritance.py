class Grandfather:
    def property(self):
        print("Zameen di")

class Father(Grandfather):
    def business(self):
        print("Business diya")

class Son(Father):
    def car(self):
        print("Car li")

s = Son()
s.property()
s.business()
s.car()