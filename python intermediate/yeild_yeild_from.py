#Why yeild
#It loads data one by one in mmeory not return complet evalue at Once;


def get_squares(n):
    result=None
    for i in range n:
        if result is None:
            result=[]
            result.append(i**2)
        return result



#It loads all the data inside the meoery at once
#if list is too big them may be ram is crashed

#Sollution is yeild
# It loads data one by one inside the memeory

def get_square(n):
    for i in range(n):
        yield i**2

        # Return function ends and dump whole dat ain memeory at once;
# But yeild function stop after generating one data and then resume from
# there only.

# Now i can call it anytime
gen=get_square(5)
next(gen)
#LAzy Evaluation

# Yeild from
def inner():
    yield 1
    yield 2

def outer():
    yield from inner()  # inner ke saare yields yahan aa jaate hain
    yield 3

# outer() se milega: 1, 2, 3



# Send is to send the data from the outside
gen=get_square(5)
print(next(gen))
print(gen.send(100))
# Value enforced 100

print(next(gen))
#101


