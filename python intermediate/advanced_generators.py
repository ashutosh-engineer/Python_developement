'''
Q5 — Ek dict comprehension likho jo list of tuples se dict banaye — 
sirf woh entries jahan value 0 se zyada ho:
data = [("apple", 5), ("banana", 0), ("mango", 3), ("grape", 0)]
# expected: {"apple": 5, "mango": 3}
'''


data = [("apple", 5), ("banana", 0), ("mango", 3), ("grape", 0)]
# dict comprehension: include only items with value > 0
dict_com = {k: v for k, v in data if v > 0}

'''
q1- a ek list comprehension hain;isme list ka sara data ke sath store hojata hain jo ki memeory hevay hain;



b-yeh ek generator expression hai isme ek bar me ek hi  record ata hain jo ki bahut lightweight hain;



q2-Yeh ek dict comprehension hain aur isme INDEX ) SE AUR ! SE VALUES AFTER FROM @split kar rahe hain;



{'a': 'hotmail.com', 'b': 'yahoo.com', 'c': 'gmail.com'}



yes yeild from generally better mana jat ahain yeild from directly function mein jitne yeilds hain sare chal jate hain:-

jaise yields from gen1():
'''