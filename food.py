from grocery import Grocery
class Food(Grocery):
    # The food class which also has an expiration date attribute.
   
    
    def __init__(self, name, price, quantity, expiration):
        super().__init__(name, price, quantity)
        self.expiration = expiration

    def show_info(self):
        print(self.name, "$", self.price, "Expires:", self.expiration)
