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
