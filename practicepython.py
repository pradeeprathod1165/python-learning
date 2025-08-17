#Variables and input/output
#1. Create a program that asks the user for their name and age, then prints:
#"Hello <name>, you are <age> years old."

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f'Hello {name}, you are {age} years old')

# Conditions
# Write a program that asks the user for a number.
# If it’s even → print "Even number"
# Else → print "Odd number"

num1 = int(input("Enter a number: "))
if num1 % 2 == 0:
    print("even number ")
else:
    print("odd number")