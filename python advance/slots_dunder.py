class Pomits:
    __slots__=('X' , 'Y')
    # So here i defined that in __dict__
    #there will be only X, 

    def __init__(self , X , Y ,  U):
        self.X=X
        self.Y=Y
        self.U=U

c1=Pomits('C' , 'D' , "W")
print(c1.X)
print(c1.Y)

# This is a feature not Any bug __slots__ restrict it;
#memoery bachata hain
#Typo se galat attricue set hone se bhi bachat ahain

