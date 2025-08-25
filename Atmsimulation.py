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

    elif choice == 2:
        deposite = int(input('enter amout to deposite:'))
        balance += deposite
        print('Deposite cash successful')
    
    elif choice == 3:
        withdraw = int(input('enter amount  to withdraw:'))

        if withdraw <= balance:
            balance -= withdraw
            print('withdraw successful',withdraw)
        else:
            print('balance not sufficient')