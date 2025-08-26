print("Hello, Bean & Bloom Cafe!")


menu = {
    "Espresso": 80,
    "Latte": 120,
    "Cappuccino": 150
}

print("Welcome to Bean & Bloom Cafe!")
for item, price in menu.items():
    print(f"{item}: ₹{price}")

choice = input("What would you like to order? ")
if choice in menu:
    print(f"{choice} will cost ₹{menu[choice]}")
else:
    print("Sorry, item not available.")


#random suggestion
import random

coffees = ["Espresso", "Latte", "Cappuccino", "Mocha", "Americano"]

print("Today's suggestion:", random.choice(coffees))


menu = {"Espresso": 80, "Latte": 120, "Cappuccino": 150}
total = 0

while True:
    order = input("Enter item (or type 'done' to finish): ")
    if order.lower() == "done":
        break
    if order in menu:
        total += menu[order]
        print(f"Added {order} - ₹{menu[order]}")
    else:
        print("Item not available.")

print("Your total bill is: ₹", total)
