#Asking for detail

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
is_Student = input("Are you a student(yes/NO): ").lower() == "yes"

#generating Profile
print("\n--- Profile Summary ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} meters")
print(f"Student: {'Yes' if is_Student else 'No'}")