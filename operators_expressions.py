print("Simple Calculator")

while True:
    # show menu every time
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    option = input("Enter the option: ")

    if option in ["1", "2", "3", "4"]:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

    if option == "1":
        print("Result:", num1 + num2)

    elif option == "2":
        print("Result:", num1 - num2)

    elif option == "3":
        print("Result:", num1 * num2)

    elif option == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero.")

    elif option == "5":
        print("Exiting...")
        break

    else:
        print("Invalid option. Please choose again.")
