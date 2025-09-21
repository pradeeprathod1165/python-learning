#Check Even or Odd
def check(n):
    return "Even" if n % 2 == 0 else "Odd"

print(check(int(input("Enter number: "))))


#Small Class Example
class Person:
    def __init__(self, name): self.name = name
    def greet(self): print("Hello,", self.name)

p = Person(input("Enter name: "))
p.greet()

#ount Vowels in a Word
count = lambda w: sum(1 for c in w if c.lower() in 'aeiou')
print(count(input("Enter word: ")))