balance = 5000

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input('enter option: '))

    if choice == 1:
        print('Balance amout : ', balance)