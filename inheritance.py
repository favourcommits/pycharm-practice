class Dad:
    def football(self):
        print("dad likes watching football")
class Mum:
    def cooking(self):
        print("mum likes cooking")
class Boy(Dad):
    def Boyage(self):
        print("The boy is 15 years old")
my_boy=Boy()
my_boy.football()
my_boy.Boyage()

class girl(Mum):
    def girl(self):
        print("The girl looks like her mother")
my_girl=girl()
my_girl.cooking()
my_girl.girl