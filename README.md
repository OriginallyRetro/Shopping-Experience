# Shopping-Experience
# A Shopping System Using Python!
import os, sys
#--- Class ---#
class consumer():
    def __init__(self, money: int, items_in_cart: list, amount_added_up = int):
        self.money = money
        self.items_in_cart = items_in_cart
        self.amount_added_up = amount_added_up

consumer = consumer(money = 100, items_in_cart = [], amount_added_up = 0)
#list
items_in_cart = []
items_bought = []
#dict
items_available = {"Steak": 20.00, "Pizza": 15.00, "Ice Cream": 13.00}

#This is where the consumer will start at
def start_menu():
    os.system("clear")
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
            os.system("clear")
            input("We hope you enjoyed your Shopping Experience!")
            sys.exit()
        case _:
            input("Invalid option")
            start_menu()
            
def browse_items():
    os.system("clear")
    input("Happy Shopping!")
    os.system("clear")
    for key, value in items_available.items():
        os.system("clear")
        print(f"Item: {key}\nCost: {value}\n===========================\n")
        match input("Type 'buy' to buy item press enter to skip: "):
            case 'buy':
                input(f"You have bought {key}.")
                items_bought.append(key)
                consumer.money -= value
                consumer.amount_added_up += value
                print(f"Current amount of money: {consumer.money}")
            case _:
                input("You have skipped over this item.")
                print(f"Current amount of money: {consumer.money}")
                
                
    print("We hope you enjoyed you Shopping Experience!")
    input()
    start_menu()
      
def current_items():
    print("Here are all of your current items along with the prices you have bought them with!:")
    
    for key, value in items_bought.items():
        print(f"Item: {key}\nCost: {value}\n**************************\n")
    
    input("Type 'ENTER' when you are finished surveying your items")
    start_menu()
    
    
    
start_menu()
            
