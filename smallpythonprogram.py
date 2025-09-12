# Simple Calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)


#age calculator
# Age after 10 years
name = input("Enter your name: ")
age = int(input("Enter your age: "))

future_age = age + 10
print(name, "you will be", future_age, "years old after 10 years.")


# Swap two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping: a =", a, "b =", b)

# Swapping logic
temp = a
a = b
b = temp

print("After swapping: a =", a, "b =", b)

# Check even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
