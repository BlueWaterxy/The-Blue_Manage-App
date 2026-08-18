# BlueWater Grocery Manger 

class Grocery:
    #  The Grocery class which sets up the name, price, and quantity attribute.
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(self.name, "$", self.price, "Quantity:", self.quantity)

    def check_price(self):
        if self.price < 0:
            self.price = 0




class Food(Grocery):
    # The food class which also has an expiration date attribute.
   
    
    def __init__(self, name, price, quantity, expiration):
        super().__init__(name, price, quantity)
        self.expiration = expiration

    def show_info(self):
        print(self.name, "$", self.price, "Expires:", self.expiration)



# A subclass of Grocery that represents drinks. It also has a size attribute. 
class Drink(Grocery):
    # The drinks class 
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

    def show_info(self):
        print(self.name, "$", self.price, "Size:", self.size)




class GroceryManager:
     # This class manages all the groceries like food and drinks. 

    def __init__(self):
        self.groceries = [
            Food("Milk", 4, 1, "Aug 20"),
            Food("Eggs", 5, 2, "Aug 25"),
            Food("Apples", 3, 6, "Aug 22"),
            Drink("Water", 2, 2, "1 gallon"),
            Drink("Orange Juice", 4, 1, "12 oz")
        ]

        self.bought = []
    #  Shows all the groceries in the list.
    def show_groceries(self):
        for grocery in self.groceries:
            grocery.show_info()

    def add_grocery(self):
        # This function adds a grocery to the list of groceries.
        name = input("What do you want to buy? ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        print("1. Food")
        print("2. Drink")

        choice = input("Choose: ")
        # Shows the user to choose between food and drink and adds the grocery to the list of groceries.
        if choice == "1":
            expiration = input("Expiration date: ")
            grocery = Food(name, price, quantity, expiration)
        elif choice == "2":
            size = input("Size: ")
            grocery = Drink(name, price, quantity, size)
        else:
            print("Please choose 1 or 2.")
            return

        grocery.check_price()

        self.groceries.append(grocery)
        self.bought.append(grocery)

        print(name, "was added!")

    def total_cost(self):

        total = 0
    #Shows the items bought and the total cost of the groceries bought.    
        print("\nThings you bought:")

        for item in self.bought:
            print(item.name, "$", item.price, "x", item.quantity)
            total = total + item.price * item.quantity

        print("Total: $", total)


# Start program

manager = GroceryManager()

while True:

    print("\n1. See groceries")
    print("2. Buy grocery")
    print("3. See what I bought")
    print("4. Quit")

    choice = input("Choose: ")
    #   Shows the groceries in the list.
    if choice == "1":
        manager.show_groceries()
    #  Adds a grocery to the list of groceries. 
    if choice == "2":
        manager.add_grocery()
    #   Shows the total cost of the groceries bought.
    if choice == "3":
        manager.total_cost()

    # Ends the program 
    if choice == "4":
        print("\n==============================")
        print("Thanks for using BlueWater's Grocery Manager!")
        print("==============================")
        break