#Encapsulation in python
#Encapsulation comes from term capusle which means binding logic and data together that they can work;
#In python generally there is no concept of private varibales;
#So we will write code with naming conventions that will suggest that this is private memeber cannot be accessed
#outside of class;

#Public memeber
class car:
    def __init__(self, color, name):
        self.color=color
        self.name=name #public member

c1=car("blue", "Cruiser")
print(c1.color)

#Protected members with naming convention cause python doesnt  have nay private varibales it cannot forcefully stop;
class man:
    def __init__(self, man_name, man_age):
        self._man_name=man_name
        self._man_age=man_age

c2=man("Ashutosh", 22)
#Now i also can acess private memeber(as per naming conventions)
#Python forcefully doesnt stops it
print(c2._man_age)

#All about protetced memebers;

#Private memebers and name mangling
#Security and name mangling and reality behind pythons private member concepts

class sec:
    def __init__(self,color, name):
        self.color=color
        self.__name=name #private not genuninly

k2=sec("blue", "sumo")
print(k2.color) # Attribute error
print(k2._sec__name) #Sumo as output 
#Now this concept is called as name mangling in python;
#Here python will rename the attribute that is started with __ but no ends with __ 
#Now here python will rename it and associate it with class like _sec__name now this can be accessed
#So the reality here is that python cant  make any private memebers it everything on naming conventions;
#Name mangling is  done to prevent accidental name exchnage in inheritance;


#Getter and setter in python

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        if new_salary < 0:
            print("Salary cannot be negative.")
            return
        self._salary = new_salary

e1 = Employee("Ashutosh", 50000)
print(e1.get_salary())    # 50000
e1.set_salary(-500)       # "Salary cannot be negative."
e1.set_salary(60000)      # works

#@property attribute
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        print("Getter called")
        # Refer to the backing field to avoid infinite recursion.
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        print("Setter called")
        # Refer to the backing field to avoid infinite recursion.
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = new_salary

e1 = Employee("Ashutosh", 50000)

print(e1.salary)      # "Getter called" then 50000 -- looks like a plain attribute access!
e1.salary = 60000     # "Setter called" -- looks like a plain assignment!
e1.salary = -500      # raises ValueError