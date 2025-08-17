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

# Lists
# Make a to-do list program (just store tasks in a list).
# Add 3 tasks
# Print all tasks

to_do_list = []
while True:
    print("1. Add task")
    print("2. view task")
    print("3. Exit")

    choice = (input("Enter your option:"))

    if choice == "1":
        task = input("enter task: ")
        to_do_list.append(task)
        print("task added successfully")
    
    elif choice == "2":
        print(to_do_list)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again.\n")


# OOP (Classes & Objects)
# Create a class Book with attributes title and author.
# Make 2 objects and print their details.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"


s1 = Book("Rich Dad Poor Dad", "Shyam")
s2 = Book("Chhava", "Ram")

print(s1)
print(s2)
