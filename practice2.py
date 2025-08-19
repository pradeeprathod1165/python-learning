#1. Variables & Input
name = input("Enter your name: ")
print(f"Hello {name}, welcome to Python!")

#2. Conditions
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
else:
    print("Zero or Negative")

#3. Loops
for i in range(1, 6):
    print("Python Rocks!", i)

#4. Function
def cube(n):
    return n**3

print("Cube of 3 is:", cube(3))

#5. List
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

#6. Dictionary
student = {"name": "Pradeep", "age": 21}
print("Student Name:", student["name"])
print("Student Age:", student["age"])

#7. Class & Object
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says Woof!")

d = Dog("Tommy")
d.bark()