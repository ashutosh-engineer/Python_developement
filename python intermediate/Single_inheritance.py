class Vehicle:
    def speed(self):
        return 200

    def fuel(self):
        return "Fuel is 50 percent"


class Car(Vehicle):
    def honk(self):
        return "Honking pooooo"



c1 = Car()
print(c1.honk())
print(c1.fuel())
print(c1.speed())