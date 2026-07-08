# un-Pythonic
if len(users) > 0:
    process(users)

# Pythonic — empty collections are falsy
if users:
    process(users)

# un-Pythonic
if x == True:
    pass

# Pythonic
if x:
    pass


#empety collections are false so need need to check conditions;
#Ternary expressions;
# regular
if age >= 18:
    status = "adult"
else:
    status = "minor"

# ternary — one line
status = "adult" if age >= 18 else "minor"

# real backend use
role = "admin" if user.is_staff else "user"
response = {"error": msg} if error else {"data": result}


# else clause on loops — rarely known, very useful
for user in users:
    if user.id == target_id
        found = user
        break
else:
    # runs only if loop completed WITHOUT hitting break
    found = None
    raise UserNotFoundError()


# never do this
for i in range(len(users)):
    print(i, users[i])

# always do this
for i, user in enumerate(users):
    print(i, user)

# zip — iterate two lists together
names = ["alice", "bob"]
scores = [95, 87]
for name, score in zip(names, scores):
    print(f"{name}: {score}")




# basic match
def handle_status(status_code):
    match status_code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:             # default — like else
            return "Unknown"
        


def handle_request(request):
    match request:
        case {"method": "GET", "path": path}:
            return handle_get(path)
        
        case {"method": "POST", "path": path, "body": body}:
            return handle_post(path, body)
        
        case {"method": method}:
            return f"unsupported method: {method}"
        

