from grocery import Grocery
from food import Food
from drink import Drink
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