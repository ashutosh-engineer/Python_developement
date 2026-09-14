class Teacher:
    def good_teacher(self):
        return "YES"

    def bad_teacher(self):
        return "NO"



class coder:
    def CP(self):
        return "YES"

    def dev(self):
        return "NO"

class person(Teacher , coder):
    pass

p1=person()
print(p1.good_teacher())
print(p1.bad_teacher())
print(p1.CP())
print(p1.dev())