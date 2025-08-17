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


# Loops
# Print all numbers from 1 to 20, but skip multiples of 3.

for num in range(1,21):
    if num % 3 != 0:
        print(num)

#Function
#Create a function square(n) that returns the square of a number.
#Ask the user for a number and print its square.

def square(n):
    return n*n

n = int(input("Enter number:"))
print("Square is :",square(n))