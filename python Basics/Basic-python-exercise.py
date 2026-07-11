
#Scenario
#-You are building a User Analytics Pipeline for a platform with 10 million users.
#Your system tracks user activity, processes events, generates reports, and enforces access control — 
# all in pure Python.

'''
Q1 — Mutability + identity + data types
A junior dev writes this session management code:
DEFAULT_SESSION = {"user_id": None, "is_active": False, "requests": []}

def create_session(user_id):
    session = DEFAULT_SESSION
    session["user_id"] = user_id
    session["is_active"] = True
    return session

s1 = create_session("user_123")
s2 = create_session("user_456")
print(s1)
print(s2)
print(s1 is s2)
Three questions:

What does s1 is s2 return and why?
What does print(s1) actually show — what is the bug?
Fix the function completely
'''

# ===== Q1 ANSWERS =====
# Question 1: What does s1 is s2 return and why?
# Answer: Returns True because both reference the SAME object in memory
# The 'is' operator checks identity (memory address), not equality

# Question 2: What does print(s1) actually show — what is the bug?
# Answer: Prints {'user_id': 'user_456', 'is_active': True, 'requests': []}
# Bug: ALL sessions reference the same DEFAULT_SESSION dict, so modifications
# to one session affect all others (shared mutable default argument problem)

# Question 3: Fix the function completely
DEFAULT_SESSION = {"user_id": None, "is_active": False, "requests": []}

def create_session(user_id):
    # FIX: Use .copy() to create independent copy of default dict
    session = DEFAULT_SESSION.copy()
    session["user_id"] = user_id
    session["is_active"] = True
    return session

s1 = create_session("user_123")
s2 = create_session("user_456")
print("\n=== Q1 Output ===")
print(f"s1: {s1}")
print(f"s2: {s2}")
print(f"s1 is s2: {s1 is s2}")  # Now returns False


'''
Q2 — Collections + slicing + performance
You have an activity log of 10 million events:
activity_log = [
    {"user_id": "u1", "event": "login", "timestamp": 1704067200},
    {"user_id": "u2", "event": "purchase", "timestamp": 1704067201},
    # ... 10 million more
]
Answer all three:

Write one line to get the last 100 events using slicing
A junior dev checks if a user is banned like this — if user_id in banned_users_list 
where banned_users_list has 1 million entries. What is the time complexity and fix it.

You need to deduplicate 10 million user IDs — write the most memory-efficient one-liner
'''
# ===== Q2 ANSWERS =====
activity_log = [
    {"user_id": "u1", "event": "login", "timestamp": 1704067200},
    {"user_id": "u2", "event": "purchase", "timestamp": 1704067201},
]

# Question 1: Get the last 100 events using slicing
last_100_events = activity_log[-100:]
print("\n=== Q2.1 Answer ===")
print(f"Last 100 events: {last_100_events}")

# Question 2: Time complexity of checking membership in banned_users_list
# Answer: O(n) — Linear time complexity (scans entire list)
# Problem: Checking 'if user_id in banned_users_list' with 1M items is slow
# Fix: Convert to set for O(1) average-case lookup
banned_users_set = set(["user_999", "user_1000"])  # O(n) to create, O(1) to check
is_banned = "user_999" in banned_users_set  # O(1) lookup
print(f"\nQ2.2 Answer: Time Complexity is O(n) for list lookup")
print(f"Fix: Use set for O(1) lookup - is_banned: {is_banned}")

# Question 3: Most memory-efficient one-liner for deduplication
user_ids = ["u1", "u2", "u1", "u3", "u2"]
unique_user_ids = set(user_ids)
print(f"\nQ2.3 Answer - Unique IDs (one-liner): unique_user_ids = set(user_ids)")
print(f"Result: {unique_user_ids}")



'''
Q3 — Generators + closures + scope
You need to generate daily reports for 50 million users. A junior dev writes:
def get_premium_users():
    all_users = list(fetch_all_users())
    return [u for u in all_users if u["plan"] == "premium"]
Four questions:

How much RAM if each user dict is 300 bytes?
Rewrite as a generator
Now wrap it in a closure that remembers how many users it has yielded so far — use nonlocal
What scope level does fetch_all_users live at in LEGB when called inside the generator?
'''
# ===== Q3 ANSWERS =====

# Question 1: How much RAM if each user dict is 300 bytes?
# Answer: 50 million users × 300 bytes = 15,000,000,000 bytes = ~14.9 GB RAM
print("\nQ3.1 Answer: 50 million × 300 bytes = 15,000,000,000 bytes (~14.9 GB)")

# Question 2 & 3 & 4: Rewrite as generator with closure + nonlocal + LEGB analysis
def get_premium_users():
    """
    Generator with closure that yields premium users and tracks count.
    Uses nonlocal to maintain counter state across calls.
    """
    counter = 0
    
    def user_generator():
        nonlocal counter
        # Simulated: all_users = list(fetch_all_users())
        # fetch_all_users is at GLOBAL (G) scope in LEGB
        all_users = [
            {"id": "u1", "plan": "premium"},
            {"id": "u2", "plan": "free"},
            {"id": "u3", "plan": "premium"},
        ]
        for user in all_users:
            if user["plan"] == "premium":
                yield user
                counter += 1
    
    return user_generator()

print("\nQ3.2 Answer: Generator implementation with closure")
premium_gen = get_premium_users()
for premium_user in premium_gen:
    print(f"Yielded premium user: {premium_user}")

print("\nQ3.4 Answer: fetch_all_users scope level in LEGB = GLOBAL (G)")


'''
**Q4 — *args/kwargs + security + control flow
You build a flexible user creation function:
def create_user(*args, **kwargs):
    db.insert("users", **kwargs)
A hacker sends this request:
create_user(
    name="ashutosh",
    email="ash@gmail.com",
    is_admin=True,
    is_superuser=True,
    role="superadmin"
)
Three questions:

What is this attack called?
What happens if you pass **kwargs directly to db.insert?
Fix the function — only allow name, email, password.
Use match/case to return different responses based on whether creation succeeded, 
failed validation, or caused a db error
'''
# ===== Q4 ANSWERS =====

# Question 1: What is this attack called?
# Answer: PRIVILEGE ESCALATION ATTACK (Attribute Injection / Mass Assignment)

# Question 2: What happens if you pass **kwargs directly to db.insert?
# Answer: Attacker can inject arbitrary fields (is_admin, is_superuser, role)
# This gives them unauthorized privileges in the database

# Question 3: Fix the function with validation and match/case
def create_user(*args, **kwargs):
    """
    Creates user with validation and error handling.
    Only allows: name, email, password
    """
    allowed_fields = {"name", "email", "password"}
    
    # Validate that only allowed fields are present
    provided_fields = set(kwargs.keys())
    invalid_fields = provided_fields - allowed_fields
    
    # Check validation
    match invalid_fields:
        case set() if not invalid_fields:
            # Validation passed - create user
            try:
                # Simulated db.insert (using dict for demo)
                user = {k: v for k, v in kwargs.items() if k in allowed_fields}
                return {"status": "success", "message": "User created", "user": user}
            except Exception as e:
                return {"status": "db_error", "message": str(e)}
        
        case _:
            # Validation failed - reject request
            return {
                "status": "validation_error",
                "message": f"Invalid fields detected: {invalid_fields}",
                "allowed_fields": allowed_fields
            }

print("\n=== Q4 Output ===")
# Valid request
result1 = create_user(name="ashutosh", email="ash@gmail.com", password="secure123")
print(f"Valid request: {result1}")

# Attack attempt (hacker trying to inject is_admin)
result2 = create_user(name="hacker", email="hack@evil.com", password="pwd", is_admin=True)
print(f"Attack attempt blocked: {result2}")


# ===== Q5 IMPLEMENTATION =====
def make_analytics_tracker(endpoint):
    """
    Creates a tracker function with closure that remembers metrics.
    
    Parameters:
        endpoint (str): API endpoint name
    
    Returns:
        function: track function that records metrics
    """
    hits = 0
    errors = 0
    total_response_time = 0.0
    
    def track(response_time, success):
        nonlocal hits, errors, total_response_time
        
        hits += 1
        total_response_time += response_time
        
        if not success:
            errors += 1
        
        avg_response_time = total_response_time / hits
        
        return {
            "endpoint": endpoint,
            "hits": hits,
            "errors": errors,
            "avg_response_time": round(avg_response_time, 2)
        }
    
    return track

print("\n=== Q5 Output ===")
tracker = make_analytics_tracker("/api/register")
print(tracker(0.23, True))   # {"endpoint": "/api/register", "hits": 1, "errors": 0, "avg_response_time": 0.23}
print(tracker(0.41, True))   # {"endpoint": "/api/register", "hits": 2, "errors": 0, "avg_response_time": 0.32}
print(tracker(0.89, False))  # {"endpoint": "/api/register", "hits": 3, "errors": 1, "avg_response_time": 0.51}



# ===== Q6 IMPLEMENTATION =====
def process_event(event):
    """
    Processes event tuple with unpacking and match/case.
    
    Handles different event types:
    - login: (event_type, user_id, ip, timestamp)
    - purchase: (event_type, user_id, ip, timestamp, price)
    - error: (event_type, user_id, error_code, message)
    - logout: (event_type, user_id, ip, timestamp)
    """
    match event:
        case ("login", user_id, ip, timestamp):
            return f"user {user_id} logged in from {ip}"
        
        case ("purchase", user_id, ip, timestamp, price):
            return f"user {user_id} purchased for {price}"
        
        case ("error", user_id, error_code, message):
            return f"error for user {user_id}: {message}"
        
        case ("logout", user_id, ip, timestamp):
            return f"user {user_id} logged out"
        
        case _:
            return "unknown event"

print("\n=== Q6 Output ===")
events = [
    ("login", "user_123", "192.168.1.1", 1704067200),
    ("purchase", "user_456", "10.0.0.1", 1704067201, 99.99),
    ("error", "user_789", "500", "db connection failed"),
    ("logout", "user_123", "192.168.1.1", 1704067210),
]

for event in events:
    print(process_event(event))



# ===== Q7 IMPLEMENTATION (MAANG HARD) =====
import time

def make_rate_limiter(endpoint, max_requests, window_seconds):
    """
    Creates a rate limiter factory with analytics.
    
    Parameters:
        endpoint (str): API endpoint name
        max_requests (int): Max requests allowed per user in window
        window_seconds (int): Time window in seconds
    
    Returns:
        function: check(user_id) that returns True if allowed, False if blocked
    """
    user_requests = {}  # {user_id: [timestamp1, timestamp2, ...]}
    total_allowed = 0
    total_blocked = 0
    call_count = 0
    
    def check(user_id):
        nonlocal total_allowed, total_blocked, call_count
        
        # Validate user_id
        if user_id is None or user_id == "":
            raise ValueError("user_id cannot be None or empty string")
        
        call_count += 1
        current_time = time.time()
        
        # Initialize user if not exists (avoid KeyError)
        if user_id not in user_requests:
            user_requests[user_id] = []
        
        # Keep only requests within time window (using list slicing)
        user_requests[user_id] = [
            timestamp for timestamp in user_requests[user_id]
            if current_time - timestamp < window_seconds
        ]
        
        # Check if allowed
        if len(user_requests[user_id]) < max_requests:
            user_requests[user_id].append(current_time)
            total_allowed += 1
            is_allowed = True
        else:
            total_blocked += 1
            is_allowed = False
        
        # Print stats after every 100 calls
        if call_count % 100 == 0:
            print(f"\n--- Rate Limiter Stats (Call #{call_count}) ---")
            print(f"Endpoint: {endpoint}")
            print(f"Total Allowed: {total_allowed}")
            print(f"Total Blocked: {total_blocked}")
            print(f"Active Users: {len(user_requests)}")
        
        return is_allowed
    
    return check

print("\n=== Q7 Output ===")
limiter = make_rate_limiter("/api/data", max_requests=5, window_seconds=10)

# Test valid requests
print("Testing valid requests:")
for i in range(5):
    result = limiter("user_1")
    print(f"Request {i+1} for user_1: {result}")

# Test blocked request
print("\nTesting blocked request (exceeds limit):")
print(f"Request 6 for user_1: {limiter('user_1')}")

# Test different user
print("\nTesting different user:")
print(f"Request 1 for user_2: {limiter('user_2')}")

# Test error handling
print("\nTesting error handling:")
try:
    limiter(None)
except ValueError as e:
    print(f"Error caught: {e}")

try:
    limiter("")
except ValueError as e:
    print(f"Error caught: {e}")