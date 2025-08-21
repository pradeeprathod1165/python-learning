#1. Reverse a String
text = "Python"
print("Reversed:", text[::-1])

#2. Factorial of a Number
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial of", num, "is", fact)

#3. Check Palindrome
word = "madam"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#4. Find Maximum in a List
numbers = [3, 7, 2, 9, 5]
print("Maximum:", max(numbers))

#5. Multiplication Table
n = 4
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#6. Simple Calculator
a = 10
b = 5
print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)

#7. Count Vowels in a String
text = "hello world"
vowels = "aeiou"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)