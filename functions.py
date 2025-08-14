def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", celsius_to_fahrenheit(c))
    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        print("Celsius:", fahrenheit_to_celsius(f))
    elif choice == "3":
        c = float(input("Enter Celsius: "))
        print("Kelvin:", celsius_to_kelvin(c))
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
