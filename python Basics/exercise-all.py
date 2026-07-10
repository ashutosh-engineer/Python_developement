'''
Your endpoint POST /api/message allows users to send messages.
 Each user can send maximum 5 messages per minute. 
You have to build the core logic in pure Python — no frameworks yet.
'''

#Question one sollution
'''
Q1 — Data types + float precision
Your rate limiter stores the timestamp of each request. A junior dev writes:

pythonimport time
request_time = time.time()    # returns float like 1704067200.123456
if request_time == 1704067200.123456:
    block_user()


Why will this comparison almost never work? What is the correct way to compare timestamps?


Answer:-We have to use decimal library  and has to compare like this
decimal(request_time)==decimal(anyhing)

Reason is that float when it comes to comparsion 
it converted into binary thats why it will always give wrong response;
-It follows IEEE Floating point conversion principle thats why;

YOu can import it like
from decimal import *

'''


#Question-2 solve

'''
Q2 — Collections + memory
You store each user's request history like this:
pythonrate_limit_store = {
    "user_123": [1704067200.1, 1704067201.3, 1704067202.7],
    "user_456": [1704067198.2, 1704067199.8]
}
Three questions about this structure:

What data type is rate_limit_store? What data type is the value for each user?
A new user makes their first request. Write the code to safely add them without a KeyError.
Why is a list the right choice here over a set for storing timestamps.

Answer-it is float;
-list is better option because ordered;
-Allow dublicates maybe at same time user logined;
-Faster insertion of Big O(1)
-
'''

pythonrate_limit_store = {
    "user_123": [1704067200.1, 1704067201.3, 1704067202.7],
    "user_456": [1704067198.2, 1704067199.8]
}

pythonrate_limit_store.update({"user" : "timestamp"})

#Question-3
'''
Q3 — Mutable default argument trap
A junior dev writes the rate limiter like this:
def track_request(user_id, history={}):
    if user_id not in history:
        history[user_id] = []
    history[user_id].append(time.time())
    return history
What is the bug? What happens after 1000 different users make requests? Fix it.
--Answer:-
Issue n the code is when 1000 of user request 1000 of new 
objects will be created and destroyed at each iteration;

-Assigning none solves this problem
-it is mutable means when new value will be added it dont create new object
but it not means when function will be called it will not take place;

'''
import time 
def track_request(user_id , history=None):
    if history is None:
        history={}
    if user_id not in history:
        history[user_id]=[]
        history[user_id].append(time.time())
        return history
    

'''
Q4 — Slicing + control flow
Your rate limiter keeps the last 10 requests per user. You need to check if the user made 5 or more requests in the last 60 seconds. Write the logic in words and code:
import time

def is_rate_limited(user_id, store):
    # user's requests are stored as list of timestamps
    # newest requests are at the end of the list
    # write your logic here
    pass
    

Conditions to handle:

User doesn't exist in store yet
User has fewer than 5 requests total
User has 5+ requests — check if 5th most recent was within 60 seconds
'''

import time

def is_rate_limited(user_id, store=None):
    if store is None:
        store = {}

    # If user doesn't exist, initialize
    if user_id not in store:
        store[user_id] = []
        return False  # not rate limited

    # Record current time
    now = time.time()
    requests = store[user_id]

    # Add current request timestamp
    requests.append(now)

    # Keep only the last 5 requests
    if len(requests) > 5:
        requests = requests[-5:]
    store[user_id] = requests

    # If fewer than 5 requests, allow
    if len(requests) < 5:
        return False

    # If 5+ requests, check time difference
    # Compare oldest of the last 5 with now
    if now - requests[0] < 60:
        return True  # rate limited
    return False

#I havent implemented all i am not able to implement it help by copilot


#Question-5
'''

Q5 — Unpacking + match/case
Your API returns different responses based on the rate limit check. 
Write a match/case statement that handles this dict:
result = check_rate_limit(user_id)
# result can be:
# {"status": "allowed", "remaining": 3}
# {"status": "blocked", "retry_after": 45}
# {"status": "error", "message": "user not found"}
Unpack the relevant value from each case and return an appropriate message string

'''

def handle(result):
    match result:
        case {"status": "allowed", "remaining": remaning}:
            return f"Remaning login trys are {remaning}"
        
        case {"status": "blocked", "retry_after": retry_after}:
            return f"Retry after {retry_after}"
        

        case {"status": "error", "message": message}:
            return message
        
        case _:
            return "unkown message"
        


        #Question-6
        
'''
**Q6 — *args/kwargs + security
A junior dev builds this flexible logging function:
def log_request(**kwargs):
    db.execute(
        "INSERT INTO logs VALUES (:data)",
        {"data": str(kwargs)}
    )

Two questions:

An attacker calls your API with extra fields
 — password=mysecret, credit_card=1234.
 Where do these end up and why is this dangerous?
Fix the function to only log safe fields — user_id, endpoint, timestamp.
'''
import sqlite3 as db
def log_request(**kwargs):
    safe_feilds=None
    if safe_feilds is None:
        safe_feilds=["user_id" , "endpoint" , "timestamp"]

        for safe in safe_feilds:
            if safe not in kwargs:
                raise ValueError(f"Missingg feild required {safe}")
            
        
    db.execute(
        "INSERT INTO logs VALUES (:data)",
        {"data" :str(kwargs)}
    )

            #Kwargs automatically converts arguements in dictionary;


    #HAcker easily explot it if got access of servers terminal
    #making it secure by adding a safety net names allowed_inputs
    #it end up dangerous by chance hacker try user=farmer is_superuser=True
    #Safety net added;


    '''
    Q7 — Generators + collections (hard)
Your system needs to generate a daily report of all rate-limited users. There are 50 million users in the database. A junior dev does:
def get_blocked_users():
    all_users = list(db.fetch_all_users())    # loads 50M users
    return [u for u in all_users if u["blocked"]]
Three questions:

How much RAM does this use if each user dict is 200 bytes?
Rewrite using a generator — just the logic in words and code
What is the difference between return and yield in this context?
    '''
def get_blocked_users():
    all_users = list(db.fetch_all_users())    # loads 50M users
    for users in all_users:
        if users["blocked"]:
            yield users


# 50 million * 200 bytes=10GB just to store users;
#What yeild doses is it  just not import whole list of rate limited users
#instead it gives user 1 by 1 so memory remanes tiny;

#Where return return everydata that matches conditions so 10 GB list to store this user;





