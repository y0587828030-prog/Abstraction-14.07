#step 1 Swimmer Inherits from Athlete
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete")

athlete = Athlete("yehosh", 26)
athlete.introduce()

class Swimmer(Athlete):
    def __init__(self,name, age):
        super().__init__(name, age)

swimming = Swimmer("tom", 22)
swimming.introduce()


## step 2 
class Athlete:
    def __init__(self, name, age,sport):
        self.name = name 
        self.age = age
        self.sport = sport

    def describe(self):
        print(f"{self.name} competes in {self.sport}")
athlete=Athlete("bob", 25, "Dance")
athlete.describe()

class Runner(Athlete):
    def __init__(self, name, age):
        super().__init__(name, age, "Running")

Ratzen=Runner("sara", 25)
Ratzen.describe()


##step 3
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete")

athlete = Athlete("yehosh", 26)
athlete.introduce()

class Cyclist(Athlete):
    def __init__(self, name, age,bike_brand ):
        super().__init__(name, age )
        self.bike = bike_brand



    def describe_gear(self):
             print(f"Cyclist {self.name} rides a {self.bike}.")

riding= Cyclist("Mike", 30, "Trek")
riding.introduce()
riding.describe_gear()

##step 4
class Athlete:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def greet(self):
        print(f"{self.name} represents {self.country}")

class Swimmer(Athlete):
    def __init__(self, name, country,stroke_style):
        super().__init__(name, country)
        self.stroke = stroke_style

class Runner(Athlete):
    def __init__(self, name, country, best_distance):
        super().__init__(name, country)
        self.best = best_distance

class Cyclist(Athlete):
    def __init__(self, name, country, race_type):
        super().__init__(name, country)
        self.race = race_type

swimming = Swimmer("Lior", "Israel", "freestyle")
running = Runner("Avi", "Kenya", "marathon")
riding = Cyclist("Jan", "France", "road")
swimming.greet()
running.greet()
riding.greet()

## step 5  Shared Warm-Up Method
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def warm_up(self):
        print(f"{self.name} is warming up.")

class Gymnast(Athlete):
    def __init__(self, name, age, apparatus):
        super().__init__(name, age)
        self.apparatus = apparatus

    def compete(self):
        print(f"hi {self.name} good look in {self.apparatus}")

class Swimmer(Athlete):
    def __init__(self, name, age, stroke):
        super().__init__(name, age,)
        self.stroke = stroke 

    def compete(self):
        print(f"hi {self.name} good look in {self.stroke}")

gym = Gymnast("Ana", 19, "rings")
swiming = Swimmer("Ben", 21, "butterfly")

gym.warm_up()
swiming.warm_up()

gym.compete()
swiming.compete()

##step 6. Constructor Chaining
class Athlete:
    def __init__(self, name, age,years_active):
        self.name = name
        self.age = age
        self.years_active = years_active

    def experience(self):
        print(f"{self.name} has been active for {self.years_active} years.")
         
class TeamSportPlayer(Athlete):
    def __init__(self, name, age, years_active, team_name):
        super().__init__(name, age, years_active)
        self.team = team_name

    def team_info(self):
        print(f"{self.name} plays for {self.team}.")

player = TeamSportPlayer("Shua", 28, 10, "biter")
player.experience()
player.team_info()

##step 7. Personal Best Tracking
class Athlete:
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport
        self.personal_best = None

    def set_record(self,value):
        self.personal_best = value
        print(f"new record: {value}")

    
    def has_record(self):
        return self.personal_best != None 

class Sprinter(Athlete):
    def __init__(self, name):
        super().__init__(name, "100m sprint")

sprint = Sprinter("Usain")

print(sprint.has_record())  
sprint.set_record(10.8) 
print(sprint.has_record())  
sprint.has_record()
print(sprint.personal_best) 

## step 8. Training Session Counter
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sessions_completed = 0

    def train(self):
        self.sessions_completed += 1 

    def sessions_needed(self, target):
        need = target - self.sessions_completed
        if need > 0:
            return need
        elif need == 0:
           return "You have arrived at your destination."
        else:
            over = self.sessions_completed - target
            return f"{over}- Number of extra workouts."   
    


class Triathlete(Athlete):
    def __init__(self, name, age, discipline):
        super().__init__(name, age)
        self.discipline =discipline

    def describe(self):
        print(f"Triathlete {self.name}, age {self.age}, discipline: {self.discipline}")

Trainee = Triathlete("Dan", 26, "cycling")
Trainee.describe()        
Trainee.train()
Trainee.train()
Trainee.train()
Trainee.train()
Trainee.train()

print(Trainee.sessions_needed(10))

print(f"{Trainee.sessions_completed} sessions completed. {Trainee.sessions_needed(10)} more needed.")


## step 9. Basketball Player Card 
class Athlete:
    def __init__(self, name, age , position):
        self.name = name
        self.age = age
        self.position = position


    def player_card(self):
        print(f"{self.name} | {self.age} | {self.position}")


class BasketballPlayer(Athlete):
    def __init__(self, name, age, position, jersey_number):
        super().__init__(name, age, position)
        self.jersey_number = jersey_number

    def full_profile(self):
        self.player_card()
        print(f"Jersey: #{self.jersey_number}")

playir1= BasketballPlayer("Mia", 24, "guard", 7)
playir1.full_profile()

playir2= BasketballPlayer("jon", 25, "guard", 9)
playir2.full_profile()

playir3= BasketballPlayer("bob", 26, "guard", 8)
playir3.full_profile()


## step 10. Three-Level Inheritance Chain
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name}.") 

class Athlete(person):
    def __init__(self, name, age, sport):
        super().__init__(name, age)
        self.sport = sport

    def train(self):
        print(f"{self.name} is training for {self.sport}.")

class ProfessionalAthlete(Athlete):
    def __init__(self, name, age, sport,sponsor):
        super().__init__(name, age, sport)
        self.sponsor = sponsor

    def sponsor_info(self):
        print(f"{self.name} is sponsored by {self.sponsor}.")

a = ProfessionalAthlete("Ronaldo", 39, "football", "Nike")
a.greet()
a.train()
a.sponsor_info()

##self larn
#1- Prevents collisions .

#2 - So that the entire system always sees 
# the same updated information, without copies

#3- Any code from anywhere can access this object.

#4- With the help of a __new__ function that checks: 
# "If we have already created the object in the past

#5- It makes it difficult to test changes that are done
#  in a single test remains

#step 1. Same Logger Object
class Logger:
    _instance = None  

    def __new__(cls):  
        if cls._instance is None:  
            cls._instance = super().__new__(cls)  
        return cls._instance  


logger1 = Logger()  
logger2 = Logger()  

print(logger1 is logger2)  


#step 2. Shared Settings
class AppSettings:
    _instance = None 

    def __new__(cls):  
        if cls._instance is None: 
            cls._instance = super().__new__(cls) 
            cls._instance.theme = "dark" 
        return cls._instance  


settings1 = AppSettings()  
settings2 = AppSettings() 

settings2.theme = "light" 

print(settings1.theme)

#step 3  Counter Singleton
class Counter:
    _instance = None  

    def __new__(cls): 
        if cls._instance is None:  
            cls._instance = super().__new__(cls)  
            cls._instance.count = 0 
        return cls._instance  

    def increment(self): 
        self.count += 1 


counter1 = Counter()  
counter2 = Counter()  

counter1.increment()  
counter2.increment()  

print(counter1.count)  
print(counter2.count) 

