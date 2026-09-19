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



