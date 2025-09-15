num1 = input("Enter a number: ")

while len(num1) > 1:  
    total = 0
    for digit in num1:
        total += int(digit)  
    print("Sum of digits =", total)
    num1 = str(total)  

print("Final single digit =", num1)
