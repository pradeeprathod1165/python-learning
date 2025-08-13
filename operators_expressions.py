print("Simple Calculator")

# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations
print("\n--- Results ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2 if num2 != 0 else "Cannot divide by zero")
print("Modulus:", num1 % num2 if num2 != 0 else "Cannot take modulus of zero")
print("Exponent:", num1 ** num2)
