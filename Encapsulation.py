#Public memeber
#it can be acessed anywhere in the class;

class ops:

    # def __init__(self, name , age):
    #     self.name=name   #Public memebr
    #     self.age=age

    #Protected member
    #Using naming convention _ before the attribute;
    #Python doesnot enforces it;
    #There is no concept of Protecting the varibale in python using naming convention not atleast like
    #language forced like in C++, Java

    # def __init__(self, car, car_color):
    #     self._car=car
    #     self._car_color=car_color

    #Private members
    #__Double underscore
    #Just naming conventions
    #Can be accesed using the __ while acessing the atttribute;
    def __init__(self , age , wage):
        self.__age=age
        self.__wage=wage




S=ops(22 ,20000)
print(S._ops__age) #Concept of name mangling
print(S._ops__wage) #Name mangling we have to pass the class also


