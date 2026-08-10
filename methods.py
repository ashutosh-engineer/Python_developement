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



#@classmethod
#Class methods are used to operate with the class level
#HEre cls is directly passed instead of any object adress(self);

class dbs:
    conductor_name="Ashutosh"

    @classmethod
    def change_conductor_name(cls, new_name):
        cls.conductor_name=new_name


e1=dbs()
e1. change_conductor_name("Sumit")
print(e1.conductor_name)

