# ##1. Describe a Menu Item

# class MenuItem:
#     def __init__(self, name, price):
#         self.name = str(name)
#         self.price = float(price)

#     def describe(self):
#         print(f"Item: {self.name} | Price: ${self.price}")

# item = MenuItem("Espresso",3.5)
# item.describe()

# ## 2. Customer Greeting
# class Customer:
#     def __init__(self, name,favorite_drink ):
#         self.name =name
#         self.favorite_drink = favorite_drink

#     def greet(self):
#         print(f"Hi! I am {self.name} and I would like a {self.favorite_drink}.")

# claint = Customer("yehosh", "coffe")
# claint.greet()

# ##3. Multiple Items with a Constructor
# class MenuItem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def describe(self):
#         print(f"Item: {self.name} | Price: ${self.price}")

# claint1 = MenuItem("latta", 4.5)
# claint2 = MenuItem("Croissant", 2.0)
# claint3 = MenuItem("Cold Brew", 5.0)

# claint1.describe()
# claint2.describe()
# claint3.describe()

# ##4. Can the Customer Afford It?
# class Customer:
#     def __init__(self, name, balance ):
#         self.name = str(name)
#         self.balance = float(balance)

#     def can_afford(self, price): 
#         return price <= self.balance

# customr = Customer("bob", 10)
# print(customr.can_afford(8.0))
# print(customr.can_afford(12.0))

##5. Track Item Stock
class MenuItem:
    def __init__(self, name, price, in_stock):
        self.name = str(name)
        self.price = float(price)
        self.in_stock = in_stock

    def sell(self):
        self.in_stock = False

    def restock(self):
        self.in_stock = True

    def status(self):
        if self.in_stock == True:
            print(f"{self.name} is in stock.")
        else:
            print(f" {self.name} is sold out.")

item= MenuItem("Muffin", 2.5, True)
item.status()
item.sell()
item.status()
item.restock()
item.status()

##6. Coffee Shop Open and Close
class CoffeeShop:
    def __init__(self, name , city,capacity ):
        self.name = name
        self.city = city
        self.capacity =capacity

    def open_shop(self):
        print(f"{self.name} is now open in {self.city}! Capacity: {self.capacity} seats.")

    def close_shop(self):
        print(f"{self.name} is now closed. See you tomorrow!")

claint = CoffeeShop("Brew House", "Tel Aviv", 40)
claint.open_shop()
claint.close_shop()

## 7. Count Item Orders
class MenuItem:
    def __init__(self, name , price):
        self.name = name
        self.price = price
        self.order_count = 0

    def order(self):
        self.order_count += 1
        print(f"{self.name} ordered. Total orders: {self.order_count}")

    def clo(self):
        self.total = self.price * self.order_count
        print(f"Total profit {self.total}") 

item = MenuItem("Cappuccino", 4.0) 
item.order()
item.clo()
item.order()
item.clo()

item.order()
item.clo()

##8. Print an Order
class Order:
    def __init__(self, customer_name, items):
        self.customer_name =customer_name
        self.items = items

    def item_count(self):
        print(f"item {len(self.items)}") 

    def print_order(self):
        print(f"Order for: {self.customer_name} ")
        for _ in self.items:
            print(f"-{_}")

custumar = Order("Dana", ["Latte", "Croissant", "OJ"])
custumar.item_count()
custumar.print_order()

## 9. Barista Shift Tracker
class Barista:
    def __init__(self, name,specialty ):
        self.name = name
        self.specialty = specialty
        self.drinks_made = 0

    def make_drink(self, drink_name):
        print(f"{self.name} made a {drink_name}.")
        self.drinks_made += 1

    def is_specialty(self, drink_name):
        return self.specialty == drink_name

    def shift_summary(self):
        print(f"{self.name} made {self.drinks_made} drinks today.")

Barista1=  Barista("Yossi", "Espresso")
Barista1.make_drink("Espresso") 
Barista1.make_drink("coffe") 
Barista1.make_drink("laata") 
Barista1.make_drink("Espresso")

print(Barista1.is_specialty("Espresso"))
Barista1.shift_summary()


        
