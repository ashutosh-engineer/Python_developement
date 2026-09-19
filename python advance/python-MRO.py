class A:
    def show(self):
        print("A")

class B(A):
    pass

B().show()
print(B.__mro__)
# (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


# c3 Linearization Algorithm
#Used By python to find classes 
'''
Child class alwasy comes before the Parrent class
Then parrent class and then class attributes
'''


class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.__mro__)

'''

(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
'''


class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from A")
        super().greet()

class C(A):
    def greet(self):
        print("Hello from A")
        super().greet()

class D(B, C):
    pass

D().greet()
# Now kiska Greet pehle chlega
# <D, B, C , A , object>



# Now understanding how super method 
# Calls according to rules of MRO


print(D.__mro__)

# Debugging MRO
# Whenever there is a bug in complex inheritance 
#Use __mro__ or mro() to check

# Super is next in MRo not direct parrent Method


