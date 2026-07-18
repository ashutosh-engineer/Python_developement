numbers = [1, 2, 3, 4, 5]

squares = []
for n in numbers:
    squares.append(n ** 2)

print(squares)  # [1, 4, 9, 16, 25]

#list comprehension
squares=[n**2 for n in numbers]

prices = [10, 25, 5, 50, 15, 3]
greater_than = [price for price in prices if price > 10]
print(greater_than)



#Dictionary compreheson;
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92},
    {"name": "Charlie", "marks": 78},
]

# name se marks ka dict banana hai
# result = {}
# for s in students:
#     result[s["name"]] = s["marks"]
result = {s["name"]: s["marks"] for s in students}
print(result)
# {"Alice": 85, "Bob": 92, "Charlie": 78}

'''
products = [
    {"id": 1, "name": "apple", "price": 10},
    {"id": 2, "name": "banana", "price": 5},
    {"id": 3, "name": "mango", "price": 25},
]

A — id se name ka dict banao — one liner
B — Sirf woh products jahan price > 8 — name: price dict banao
'''

products = [
    {"id": 1, "name": "apple", "price": 10},
    {"id": 2, "name": "banana", "price": 5},
    {"id": 3, "name": "mango", "price": 25},
]

id={s["id"]: s["price"] for s in products if s["price"] > 8}
print(id)

emails = ["a@gmail.com", "b@yahoo.com", "c@gmail.com", "d@yahoo.com"]
unique_domain = {email.split("@")[1] for email in emails}
print(unique_domain)