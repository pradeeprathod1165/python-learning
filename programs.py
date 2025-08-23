#1. Fibonacci Series (using loop)
# Fibonacci series up to n terms
n = 10
a, b = 0, 1

print("Fibonacci series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


#2. Palindrome Checker
# Check if a string is a palindrome
word = "radar"
if word == word[::-1]:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

#3. Simple Calculator (with functions)
# Simple Calculator
def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y != 0 else "undefined"

print("Add:", add(5, 3))
print("Subtract:", sub(5, 3))
print("Multiply:", mul(5, 3))
print("Divide:", div(5, 3))