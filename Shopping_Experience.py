import os, sys

#--- Class ---#
class Consumer:
    def __init__(self, money: int, items_in_cart: list, amount_added_up = int):
        self.money = money
        self.items_in_cart = items_in_cart
        self.amount_added_up = amount_added_up

consumer = Consumer(money=100, items_in_cart=[], amount_added_up=0)

# List and dictionary for items
items_in_cart = []
items_bought = {}
items_available = {"Steak": 20.00, "Pizza": 15.00, "Ice Cream": 13.00}

# This is where the consumer will start at
def start_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("---------------------------------")
    print("Welcome to the Shop Program!")
    print("============================")
    print(f"Current amount of money: {consumer.money}")
    print("[1] Browse and Buy Items")
    print("[2] View your current items")
    print("[3] Leave the Store")
    match input("Pick your option dear consumer: "):
        case '1':
            browse_items()
        case '2':
            current_items()
        case '3':
            os.system("cls" if os.name == "nt" else "clear")
            input("We hope you enjoyed your Shopping Experience!")
            sys.exit()
        case _:
            input("Invalid option")
            start_menu()
            
def browse_items():
    if consumer.money <= 13.00:
        input("You do not have enough money to shop")
        os.system("cls" if os.name == "nt" else "clear")
        start_menu()
    
    input("Happy Shopping!")
    os.system("cls" if os.name == "nt" else "clear")
    for key, value in items_available.items():
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Item: {key}\nCost: {value}\n===========================\n")
        match input("Type 'buy' to buy item press enter to skip: "):
            case 'buy':
                input(f"You have bought {key}.")
                items_bought[key] = value
                consumer.money -= value
                consumer.amount_added_up += value
                print(f"Current amount of money: {consumer.money}")
            case _:
                input("You have skipped over this item.")
                print(f"Current amount of money: {consumer.money}")
                
    print("We hope you enjoyed your Shopping Experience!")
    input()
    start_menu()
      
def current_items():
    os.system("cls" if os.name == "nt" else "clear")
    print("Here are all your items you have bought along with the prices attached to said items.")
    
    if items_bought:
        for key, value in items_bought.items():
            print(f"Item: {key}\nCost: {value:}\n**************************\n")
        input("Type 'ENTER' when you are finished surveying your items")
    else:
        input("You have no items to survey. Press ENTER to return to the main menu.")
    
    start_menu()
    
start_menu()
