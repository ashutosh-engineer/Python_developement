#  Collections: list, tuple, dict, set, frozenset

# lists
# lists are orderd/mutable/allow duplicate
# In memeory implemented as dynamic array
# Memeory allocated while runtime;

my_list=[1,2,3,4,5,6,67,8,8]
print(my_list)

my_list.append(2) #Big O(1)-Operation
my_list.insert(1,3) #Big O(n) operation because every elemnt has to 
# transfer right
print(my_list)


# Tuple
# ordered,immutable,allow duplicates, faster than lists
# example to store cordinates as it cant changes;
# can be used as key also
tuples_c=(10,10) #Tuple
dict={(19.0760, 72.8777):"Mumbai"} #As passed as key-Tuple

print(dict)


#Dictionaries are orderd, mutable, implemented as hash-tabel in memory
name_dict={
    "id":1,
    "Name":"Ashutosh Singh"
}

print(name_dict)
#Convert list into dicts for fast lookup always 



#sets
# stes are unordered,mutable as well dont allow duplicate
tags={"python" ,"c","cpp"}
tags.add("python")
print(tags)
#{'cpp', 'python', 'c'} output clarly shows unorderd
#everytime you print there will be different order

#frozenset
# Immutable version of set
#where on every modification there will be an more object in memory 


'''
Q1 — Why can't you use a list as a dictionary key but you can use a tuple? 
What property makes something usable as a dict key?

Answer:-Tumples are immutable;Means their content never changes;
So their hash never changes;
'''

'''
You have an API endpoint that receives 10,000 user IDs and needs to check
which ones exist in your database 
(which returns a list of 50,000 valid IDs). 
Write the logic in words — should you use a list or
set for the valid IDs, and why?

-I will use sets;
sets store only unique values;
sets lookup operation are in Big O(1) because uses hash table where list uses Big O(n) operations;
'''

'''
total = ""
for i in range(10000):
    total = total + str(i)

It is big mistake;
it is creating this much time 10000 new object in memory and dstroys it;
strings are immutable means data never chnages if chnages then new object
will be created;

result = "".join(str(i) for i in range(1000)) join at end;
'''

'''
Q4 — You are storing product prices in your Flask API. 
A user reports that price == 0.3 is returning False even though the price is clearly 0.3.
 What is the bug and how do you fix it?

 -In python we have to use decimal for it.
 that is from decimal import *
 because flaot follows IEEE precision floating point priciple.
 where each number  is converted in binary so output never matches;
'''