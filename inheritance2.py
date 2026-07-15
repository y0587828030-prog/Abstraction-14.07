##1. Swimmer Inherits from Athlete
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete.")

class Swimmer(Athlete):
    def __init__(self, name, age):
        super().__init__(name, age)

swimeir = Swimmer("Tom", 22) 
swimeir.introduce()

##2. Runner with a Fixed Sport
class Athlete:
    def __init__(self, name, age, sport):
        self.name = name
        self.age = age
        self.sport = sport

    def describe(self):
        print(f"{self.name} competes in {self.sport}.")

class Runner(Athlete):
    def __init__(self, name, age ):
        super().__init__(name, age, "Running" )

runner =  Runner("Sara", 25)
runner.describe()