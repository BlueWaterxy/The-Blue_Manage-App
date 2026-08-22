# Grocery blueprint

class Grocery:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(self.name, "$", self.price, "Quantity:", self.quantity)

    def check_price(self):
        if self.price < 0:
            self.price = 0