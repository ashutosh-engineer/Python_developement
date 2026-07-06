#  Data types: int, float, str, bool, None

x=9999999999999999
print(x *x )

# There are no size of integer in python.it works perfectly fine and does not overfolow;
# Untill your ram allows it;

# This is helpfull in backend while handling large calculation values as well as
# the cryptographic Encryptions;

# float
# float uses IEEE standard precision.

x=0.1+0.2
y=0.3    
# The reason that we cannot use is here that it compares identity not equality
# Sometimes it caches result and show true if x,y both inputs are 0.3 and 0.3 it will always show true;
if x == y:
    print("True")
else:
    print("False")

# Always false 0.1 , 0.2ver represented in binary this way.
# This can became catatstrophic in financial system that why there is Decimal been used;
# from decimal import Decimal


# str-also known as string
# unicode charector-handle a;ll languages by default
# it is immutable;
# catastophic is when someone perform concatenation operation , on every 
# operation it creates an new object and then destroy it.

a="uvwxyz"
emoji="🚀"
name="अशुतोष" 

print(len(emoji)) #always 1


# bool-also known as bolean
# Always print true, false;
# True=1,false=0
# lets prove values of bolean

yes=True
no=False
print(yes + no) #output 1 because 1+0=1
# so much used where just confirmation needed it is true or false;

# none
# it is use to show that there is no vale means null;
# lets demonstarte it

list_dict=[]
list_dict.append(None)
print(list_dict) #oputput will be [None]