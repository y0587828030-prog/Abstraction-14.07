##1. Describe a Menu Item

class MenuItem:
    def __init__(self, name, price):
        self.name = str(name)
        self.price = float(price)

    def describe(self):
        print(f"Item: {self.name} | Price: ${self.price}")

item = MenuItem("Espresso",3.5)
item.describe()

## 2. Customer Greeting
class Customer:
    def __init__(self, name,favorite_drink ):
        self.name =name
        self.favorite_drink = favorite_drink

    def greet(self):
        print(f"Hi! I am {self.name} and I would like a {self.favorite_drink}.")

claint = Customer("yehosh", "coffe")
claint.greet()

##3. Multiple Items with a Constructor
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(f"Item: {self.name} | Price: ${self.price}")

claint1 = MenuItem("latta", 4.5)
claint2 = MenuItem("Croissant", 2.0)
claint3 = MenuItem("Cold Brew", 5.0)

claint1.describe()
claint2.describe()
claint3.describe()