class MenuItem:
    def __init__(self, name, price):
        self.name = str(name)
        self.price = float(price)

    def describe(self):
        print(f"Item: {self.name} | Price: ${self.price}")

item = MenuItem("Espresso",3.5)
item.describe()