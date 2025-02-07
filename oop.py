# object oriented programming
class Person:
    def __init__(self, name, age):
        # this is a constuctor method
        # it takes two parameters and initialise it as attribute
        self.name = name
        self.age = age
    def myfunction(self):
        print(f"Hello my name is {self.name}, and my age is {self.age}")
        #this is a method function
#create an object or an instance of a class
myobj=Person("John", 36)
myobj.myfunction()
myobj2=Person("Velex", 6)
myobj2.myfunction()
myobj3=Person("Alehandro", 56)
myobj3.myfunction()
myobj4=Person("Joy", 3)
myobj4.myfunction()
myobj5=Person("Alehand", 5)
myobj5.myfunction()