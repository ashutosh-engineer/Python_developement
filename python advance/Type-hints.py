# Type hint scan be used inside functions
# Can be use inside classes , lists
def add(a:int , b:int) -> int:
    return a+b

add(2,4)


# List-Type hints
nums: list[int]= [1,2,3]

# Tuple type hints

point: tuple[int , int]=(10, 20)

# Dictionary type hints
student: dict[str , int]={
    "Ashutosh" : 21
}