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
