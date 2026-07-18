users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": True},
    {"name": "Dave", "active": False},
]

def get_active_users(users):
    for u in users:
        if u["active"]:
            yield u


gen = get_active_users(users)
names = [user["name"] for user in gen]
print(names)
