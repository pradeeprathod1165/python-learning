num1 = input("Enter a number: ")

while len(num1) > 1:  
    total = 0
    for digit in num1:
        total += int(digit)  
    print("Sum of digits =", total)
    num1 = str(total)  

print("Final single digit =", num1)


#multiplication table
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
