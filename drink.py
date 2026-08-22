from grocery import Grocery
# A subclass of Grocery that represents drinks. It also has a size attribute. 
class Drink(Grocery):
    # The drinks class 
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

    def show_info(self):
        print(self.name, "$", self.price, "Size:", self.size)