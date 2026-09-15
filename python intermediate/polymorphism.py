# Common polymorphism

class car:
    def finale(self):
        return "Honks"

class nema(car):
    def finale(self):
        return "Ashutosh"

class Finale(car):
    def finale(self):
        return "At SIH"

lists = [Finale(), nema(), car()]
for item in lists:
    print(item.finale()) #Method overriding is mandotry here



#Function polymorphism.
class Pen:
    def use(self):
        return "Writing"

class Eraser:
    def use(self):
        return "Erasing"

def perform_task(tool):
    print(tool.use())

perform_task(Pen())
perform_task(Eraser())