#Topics covered:-Functions: Scope (LEGB), Closures, nonlocal
#LEGB-In python when you  declare any varibal epython searches it in definite order that order is 
#LEGB order;
#L-Local
#E-Enclosing
#G-Global
#Builtin;

#local scope
def counter():
    counter = 0 #local varibale;
    if counter:
        counter += 1
    return counter

counter()
print(counter) #Non-acessible

#Global scope
#In this we can acess varibale thorugh al over program
#Inside function if we are trying to modify value we have to us global keywoords;

name_count=2
def print_name_count():
    global name_count
    name_count=3

print_name_count()
print(name_count) #This varibale will also be accessable outside of function


#Built-in functions
#Functions those which are builtin inside the python are builtin functions;
len()#These are builtin functions pre provided by python
id()#These are builtin functions pre provided by python


#Builtin functions are so use-full it reduce headche of writing code for multiple tasks;


#Enclosures;
#It only exist when you hve a function inside a function;

def print_message():
    name="hello" #local varibale but enclosure varibale;

    def helper_printer():
        print(name)

    helper_printer()
print_message()



#Closures;
#A closure in function which remeber a varibale evern after outer function is destroyed;
#__closure__ attribute works internally in this


def make_multiplier(factor):
    def multiply(number):
        return number * factor      # factor is from enclosing scope
    return multiply                 # returning the inner function itself

double = make_multiplier(2)     # outer function runs, returns inner function
triple = make_multiplier(3)

# make_multiplier is done — but factor is still alive inside the closures
double(5)       # 10 — factor=2 remembered
triple(5)       # 15 — factor=3 remembered
double(10)      # 20

#double tripele are enclosures;

#How closure works internally
def add(x):
    def made_add(n):
        return n+x
    

add5=add(5)
double.__closure__
double.__closure__[0].cell_contents

#Pythonn stores enclosing varibale in a cell object which it have refrence of;
#It doesnt have refrence of the varibale;

#non-local keyword;

def counter():
    count = 0

    def increment():
        nonlocal count      # use the enclosing count, not a new local
        count = count + 1
        return count

    return increment

c = counter()
c()     # 1
c()     # 2
c()     # 3


#Now queston answer in this;
'''
Q1 — What does LEGB stand for and in what order does Python search? 
Give one real example of each scope level.

LEGB stand for local ,enclosure.global,builtin

'''
#local scope
def counter():
    counter = 0 #local varibale;
    if counter:
        counter += 1
    return counter

counter()
print(counter) #Non-acessible


'''
 What is the output of this and why:
pythonx = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
    print(x)

outer()
print(x)
--Output should be:-
When function will call itself it will print local;
This is an enclosure varibale;
it will print local then enclosing

But print(x ) which written outside is not going to work cause that is an local varibale;
'''

'''
Q3 — What is the output of this and why:
x = 10

def change():
    x = x + 1
    return x

change()

-Will give na error
-We have to use global varibale if we have to modify the value inside the function
'''
Q3 — What is the output of this and why:
pythonx = 10

def change():
    x = x + 1
    return x

x=10
def change():
    global x
    x=x+1
    return x

change()

#11 wil be printed;

'''
Q4 — Write a closure called make_greeting that takes a 
language parameter and returns a function that takes a name and returns a greeting.
 Support "english" and "hindi". Example: make_greeting("hindi")("Ashutosh") should return "Namaste Ashutosh".
'''

def make_greeting(language):
    language = language.lower()

    def greet(name):
        if language == "hindi":
            return f"Namaste {name}"
        return f"Hello {name}"

    return greet


make_greeting("hindi")("Ashutosh")

'''
Issue discovery

def make_counter():
    count = 0
    def increment():
        count += 1
        return count
    return increment

    use of non-local keyword mandotry
    cause python treat it like global only
    so non-local tell that no new local varibal is this
'''

def make_counter():
    count=0;
    def increment():
        nonlocal count
        count+=1
        return count
    return increment()

'''
Q6 — Explain in your own words
 what is the difference between global and nonlocal? When would you use each?

  use of non-local keyword mandotry
    cause python treat it like global only
    so non-local tell that no new local varibal is this
 -
'''