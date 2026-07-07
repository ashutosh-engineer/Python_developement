def register(name, email, dob, errors=[]):
    if not email:
        errors.append("email required")
    return errors
    
    
    
    #Lists are immutable/so this step prevent from data leaks also;
    #reason:-because everytime an new object will be created in memory and destroys it whenever email is not present there;
def register(name ,email,dob , errors=None):
    if errors is None:
        errors=[]
        if not email:
            errors.append("Email Required")
            
            
#I skipped generator and left to learn it but i know;
#Generator function uses something called yeild keyword that maintain the consistency of iteration while list crashes;
#Constant time operation as well as per iteration single user produced;


#First of all list is implemented as dynamic array in memory means lookup time will be Big O(n);


#Question 4-is on SQL injection but we havent learnt querries and all
#-Float always uses IEEE principle of floating point precision
#So when value converted to binary then there sum will never equal to 0.3.

#to implement this we have to use decimal that is from decimal import Decimal
fee = 0.10 + 0.20 
if fee == 0.30:
    charge()
    
    
 #This is disastourous -Lookup time in list is Big O(n) reason it is
 #implemented as the dynamic arrays in the memory;
 
 #This process will consum elot of time;
 #
if email.split("@")[1] in set(banned_list)  # banned_list is a list
#I cant optimize it cause i didnt learned these implementation yet
