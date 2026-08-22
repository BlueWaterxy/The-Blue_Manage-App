# Start program
from grocery_manager import GroceryManager
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
     