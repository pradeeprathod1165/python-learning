#string operations
text = 'Python programming'

print(text[1])
print(text[-1])
print(text[0:6])
print(text.upper())
print(text.lower())
print(text.replace("Python", "Java"))
print('ing' in text)


#while loop
i = 1
while i <= 5:
    print("Count:", i)
    i += 1

#break and continue *(control loop)
for i in range(1,10):
    if i == 5:
        break
    print(i)

for j in range(1,11):
    if j == 5:
        continue
    print(j)

#Functions with Multiple Arguments & Defaults
def mularg(base, exp = 2):
    return base ** exp

print(mularg(3))

#class and object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name:", self.name, "Age:", self.age)

s1 = Student("Pradeep", 21)
s1.display()

#built in library
import math
print(math.sqrt(16))    
print(math.factorial(5))

import random
print(random.randint(1, 10))  