class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal constructor: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # parent ka constructor call
        self.breed = breed
        print(f"Dog constructor: {self.breed}")

d = Dog("Tommy", "Labrador")



# Parrent method calling
class type:
    def type(self):
        print("Type is Harry")

class type_note(type):
    def des(self):
        super().type()
        print("This is my type")


t=type_note()
t.des()


# Constructor chaning
class A:
    def __init__(self):
        print("A is a constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("Bs constructor")

class C(B):
    def __init__(self):
        super().__init__()
        print("Cs  constrcutor")

C()