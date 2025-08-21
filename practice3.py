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