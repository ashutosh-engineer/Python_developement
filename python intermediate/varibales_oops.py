class Employee:
    count_emp = 0  # class variable

    def __init__(self, employe, name):
        self.employe = employe  # instance variables
        Employee.count_emp += 1
        self.name = name  # instance variables

    @classmethod
    def reset_count(cls):
        cls.count_emp = 0
        return cls.count_emp



e1 = Employee("Software Engineer", "Ashutosh Singh")
print("Employee details:", e1.employe, e1.name)

print("Employee count:", e1.count_emp)

print("Reset count:", Employee.reset_count())
print("Employee count after reset:", Employee.count_emp)
