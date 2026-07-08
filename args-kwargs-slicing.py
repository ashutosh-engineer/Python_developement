#list-indexing
users = ["alice", "bob", "charlie", "dave", "eve"]
print(users[1:3]) #till charlie;
print(users[:1]) #alice
print(users[::-1]) #Reversed;
#using slice keyword;
first_three=slice(0,3)
print(users[first_three])


#Real-life uses are their of slicing in backend;
email="ashutoshsingh6376@gmail.com"
name=email[:13]
domain=email[18:27]
email.split("@")[1]

print(name)
print(domain)



#Unpacking;
#unpacking is  moving elemnt from sequence;
a , b=1,2
a , b=b,a #Swapping without using temp varibale;
print(a) #2
print(b) #1


#*unpacking
start , *middle , end=[1,2,3,4,5,6,7,8,9,10,11,12]
print(start)
print(middle)
print(end)

#loop unpacking
users = [("alice", 25), ("bob", 30), ("charlie", 22)]
for name, age in users:
    print(f"{name} and {age}")


#nested loop unpacking
data = [("alice", (19.07, 72.87)), ("bob", (28.61, 77.20))]
for name ,(lat ,long) in data:
    print(f"{name} and {lat} and {long}")




#args/kwargs
#*args-varibale poitional Arguement
#**kwargs varibale dictionary arguement

def add(*addi):
    return sum(addi)


print(add(1,2))

#This will be dangeorous if isnstea dof print there will db.execute
#As well as if you do this always make an list of allowed commands;
def querry(**kwargs):
    print("INSERT INTO db;")


querry(id=2 , is_superuser=True)
#it convert it into the dictionary;