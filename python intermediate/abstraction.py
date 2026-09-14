# from abc import ABC, abstractmethod

# #abstract base class is implemented using abc model and abstract method
# class Greet(ABC):
#     @property
#     @abstractmethod
#     def make_sound(self):
#         pass   #abstract method

#     #Concreate method
#     def moving(self):
#         return "moving"


# class English(Greet):
#     @property
#     def make_sound(self):
#         return "Bark"

# g=English()
# print(g.make_sound)


#We cannot instanitate an abstract Base class

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    # Concrete method
    def describe(self):
        return "I am a geometric shape"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# Example usage
shapes = [
    Circle(5),
    Rectangle(10, 4),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(shape.describe())
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
    print("---")
