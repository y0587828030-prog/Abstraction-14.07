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

##3. Cyclist with Gear Info
class Athlete:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete.")

class Cyclist(Athlete):
    def __init__(self, name, age,bike_brand):
        super().__init__(name, age)
        self.bike_brand = bike_brand

    def describe_gear(self):
        print(f"Cyclist {self.name} rides a {self.bike_brand}.")

cyclist = Cyclist("Mike", 30, "Trek")
cyclist.describe_gear()


##4. Three Sports, One Parent
class Athlete:
    def __init__(self, name , country):
        self.name = name
        self.country = country

    def greet(self):
        print(f"{self.name} represents {self.country}")

class Swimmer(Athlete):
    def __init__(self, name, country,stroke_style):
        super().__init__(name, country)
        self.stroke_style =stroke_style

class Runner(Athlete):
    def __init__(self, name, country,best_distance):
        super().__init__(name, country)
        self.best_distance = best_distance

class Cyclist(Athlete):
    def __init__(self, name, country, race_type):
        super().__init__(name, country)
        self.race_type =race_type

swimmer = Swimmer("Lior", "Israel", "freestyle")
swimmer.greet()
runner = Runner("Avi", "Kenya", "marathon")
runner.greet()
cyclist= Cyclist("Jan", "France", "road")
cyclist.greet()

## 5. Shared Warm-Up Method
class Athlete:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def warm_up(self):
        print(f"{self.name} is warming up.")

class Gymnast(Athlete):
    def __init__(self, name, age, apparatus):
        super().__init__(name, age)
        self.apparatus = apparatus

    def compete(self):
        print(f"{self.name} competes on the{self.apparatus} good look!! ")

class Swimmer(Athlete):
    def __init__(self, name, age, stroke):
        super().__init__(name, age)
        self.stroke = stroke

    def compete(self):
        print(f"{self.name} competes on the{self.stroke} good look!! ")

gymnast =Gymnast("Ana", 19, "rings")
gymnast.warm_up()
gymnast.compete()

swimer =Swimmer("Ben", 21, "butterfly")
swimer.warm_up()
swimer.compete()