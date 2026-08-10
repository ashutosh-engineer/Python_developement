#instance method
#Method which uses object data to process called as the instance method;
#Dpened on attributes data

class Employee:
    def __init__(self, name , salary):
        self.name=name
        self.salary=salary

    def give_increment(self, amount):
        self.salary+=amount

        print(f"{self.name} and the salary is {self.salary}")

e1=Employee("Ashutosh", 3500)
e2=Employee("Sumit", 2000)
e1.give_increment(5000)
print(e1.name)
print(e1.salary)
print(e2.salary)
e2.give_increment(2000)



# @classmethod
# Class methods are used to operate with the class level
# HEre cls is directly passed instead of any object adress(self);

class dbs:
    conductor_name="Ashutosh"

    @classmethod
    def change_conductor_name(cls, new_name):
        cls.conductor_name=new_name


e1=dbs()
e1. change_conductor_name("Sumit")
print(e1.conductor_name)



#Static methods
#static methods are the methods that dont rely on cls attribut eor instance attributes like @classmethod
#or static methods
#it is wrapped in a class to show that method is logically belong to the same class only;
#no self passed or cls passsed just need attibuut eto work on;

class mechnaic:
    def __init__(self, mechanic_name, mechanic_salary):
        self.mechanic_name=mechanic_name
        self.mechnaic_salary=mechanic_salary

    @staticmethod
    def check_salary(mechanic_salary):
        return mechanic_salary >= 2500


e1=mechnaic("Ashutosh", 2500)
print(e1.check_salary(2500))


#Bounds method
e1 = Employee("Ashutosh", 50000)

method_ref = e1.give_raise   # NOT calling it yet -- just referencing it
print(method_ref)   
# <bound method Employee.give_raise of <__main__.Employee object at 0x...>>

method_ref(5000)   # this works exactly like e1.give_raise(5000)