'''
Q1 — What is the output and why:
a = [[1, 2], [3, 4]]
b = a[:]
b[0][0] = 999
print(a)


Answer:-it will give updates list  of [[999,2] , [3,4]]
-Also lists are mutable and allow duplicates (Writing just for my knowledge)
-when you write b[0][0] means you are refreing to the list which is in index 0 then elemnt which is in
index 0 of list 0;
And where you written a[:] here you dont given the start or stop vlue leave jump so it soes nothing;
'''
a = [[1, 2], [3, 4]]
b = a[:]
b[0][0] = 999
print(a)


'''
What does this print and why:
first, *middle, last = [10, 20, 30, 40, 50]
print(middle)

it print 10
20 20 40
50 

this is called as star unpacking;
where you have assigned first to th first value of list and last to the last value of list
and else assigned to *middle;
'''

first, *middle, last = [10, 20, 30, 40, 50]
print(middle)

'''
Q3 — A Flask endpoint receives this dict from a request:
payload = {"name": "Ashutosh", "email": "ash@gmail.com", "age": 21}
Write one line to call register(name, email, age) using unpacking.

register(**payload)-Kwargs unpacking-I dont know it
I have done earlier it using string literals unpacking method;
'''

def log_event(event_type, *details, timestamp):
    print(event_type , details, timestamp)

    #You cannot pass timestamp after variadic positional Arguement until denoted it as keyword;

log_event("login", "user123", "192.168.1.1", timestamp="2024-01-15")





'''
 Write a match/case statement that handles an API response dict — 
 if it has a "data" key return the data, 
 if it has an "error" key return the error message, otherwise return "unknown response".
'''

def response(data):
    match data:
        case {"data": d}:
            return d
        case {"error": msg}:
            return msg
        case _:
            return "unknown response"