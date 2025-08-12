# Getting user input
age = input("Enter your age: ")

# Checking type before conversion
print("Type before conversion:", type(age))

# Converting string to int
age = int(age)
print("Type after conversion:", type(age))

# Using different data types
name = input("Enter your name: ")
height = float(input("Enter your height in meters: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

# Displaying information
print("\n--- Your Details ---")
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Is Student:", is_student, "| Type:", type(is_student))
