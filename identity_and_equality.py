#variales
#mutabilty
#Identity    
#GIL

'''
in python eveything is object that point to certain memeory adress;
Varibales-are the name of memory adress or point to certain memeory adress;

Varibales are the conatiner that holds the data;
'''

'''
mutabilty means where data can be get changed, it will not create new object;
inmutbale means if data modified it will create an new object
'''
# Immutable;
x="Hello"
print(id(x))

x=x+"byebye"
print(id(x))


# Mutable;
my_list=[2,3,4,5]
print(id(my_list)) 

my_list.append(26)
# print(my_list)
print(id(my_list))


# identity vs equality
x=24
y=24
if(x==y):   #equality
    print("true")

def check(x,y):
    if x is y :
        return True;
#checks identity and gives false;
check(2,2)

'''
equality checks at values but identity check  objects thats why in is case it will fail;
'''


'''
Refrence counting where it checks how many varibales refrence or point to same memory block or object;
'''