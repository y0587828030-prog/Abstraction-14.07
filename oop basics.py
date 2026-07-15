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