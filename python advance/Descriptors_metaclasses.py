class Descriptor:
    def __get__(self, instance, owner):
        return ("GET Called")
        return 42

class myclass:
    x=Descriptor()  
    # x is object here


obj=myclass()
print(obj.x)



#Descriptors Protocols
class descriptor:
    def __get__(self , instance , owner):
        if instance is None:
            return self
        return instance._value

    def __set__(self , instance , value):
        instance._value=value

    def __delete__(self , instance):
        del instance._value

class myclass:
    x=descriptor()


clst=myclass()
clst.x=10
# setter
print(clst.x)
# getter
del clst.x
# Delete descriptor value