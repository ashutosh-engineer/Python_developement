#list comprehension
squares=[]
for x in range(10):
    squares.append(x**2)

#comprehension
squares=[x**2 for x in range(10)]


#Comprehensions with the conditions;
users=[]
premium= [x for x in users if x['type']=="premium"]

# list se dict banana — O(1) lookup ke liye
users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
user_map = {u["id"]: u for u in users}
user_map[1]   # instant lookup

# dict values transform karna
prices = {"apple": 10, "banana": 5, "mango": 20}
discounted = {k: v * 0.9 for k, v in prices.items()}

# dict filter karna
expensive = {k: v for k, v in prices.items() if v > 8}

# unique domains from emails
emails = ["a@gmail.com", "b@yahoo.com", "c@gmail.com"]
domains = {e.split("@")[1] for e in emails}
# {"gmail.com", "yahoo.com"}

# unique event types from logs
event_types = {log["event"] for log in logs}