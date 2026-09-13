#Here will talk about object creation flow in python;
'''
__new__ creates the raw object
the data returned from __new__ passed as self in __init__method

__init__method actually feeds the constructor
-it initalizes object with the value

__now__ when an object is created and we have to dleet eit then
__del__ emthod is used it wont run untill the 
refrennce count is 0;

We use del keyword for it;
It reduces the refrence count By 1 ;

Memeory get freed
like in c we call free(ptr)
'''

#varibales
'''
1.Class varibales
2.Instance varibales
3.Local varibales
'''

class Car:
    car_type="SUV"
    #Class varibale

    def __init__(self, car, brand):
        self.car = car
        self.brand = brand
        Car.car_type = "Sports Car" # Enforce changed
        # It shows class variable can be shared among all the methods
        # and also shows how to access it;

        self.tc_count = 0 # instance variable;

    #Local varibale which is just  create dinside a functions or method
    @classmethod #We have to add decorator so function can 
    #understand that this is a classmethod ;
    def chnage_car_type(cls):
        cls.car_type="Cruiser"

        #ocla varibales cannot accessed outside of the method
        


#Methods 
'''
A function is inside a class will be called as the method
what ever function you write under a class wil be a method;

1.Instance MEthods
2.Class methods
3.Static  methods
4.Bound methods;

We will Learn the rules of using decorators also here;
'''

#instance method
'''
Instance methods use data of instance only to
perform any of the operations.
'''

class Salary:
    def __init__(self , name , salary):
        self.name=name
        self.salary=salary

    def calculate_salary(self , amount):
        self.salary+=amount
        print(f"The name is {self.name} and the incremented salary is {self.salary}")


sal=Salary("Ashhutosh" , 3600)

print(sal.calculate_salary(3600))

#Instanc method done


#class method now
class caar:
    car_type="SUV"


    @classmethod
    def car_types(cls):
        cls.car_type="Maruti"


#static method
'''
So it is method which shows that belonging to the class 
actually performing some validation or anything
'''

class Emp:
    def __init__(self, salary):
        self.salary=salary

    @staticmethod
    def checks_salary(salary):
        return salary > 3000

#It will give true or false

e1=Emp()
print(e1.checks_salary(2000)) #output false;


#Bound not that much imprtant but it is bounded to an method only;

