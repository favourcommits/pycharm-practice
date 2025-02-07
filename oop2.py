# using oop create a class called cars that has the
# following attribute, model,colour and year of manufacturer.Implement constructor
# method and a method function that
# that prints "my favourite car is","it is colour" "and manufactured in the year"
# create 5 instance of that class



class cars:
    def __init__(self,model,colour,year):
        self.model = model
        self.colour = colour
        self.year = year
    def mywork(self):
        print(f"my favourite car is {self.model} , its colour is {self.colour} and it was manufactured in the year {self.year}")
mycar = cars("Mercedez","blue",1999)
mycar.mywork()
mycar = cars("Random","red",year=2020)
mycar.mywork()
mycar = cars("Toyota","black",2009)
mycar.mywork()
mycar = cars("Lamborghini","blue",2015)
mycar.mywork()