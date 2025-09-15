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

#count digits
n2 = (input("Enter number: "))
count = 0

for digit in n2:
    count += 1

print(count)

#even number till N
n3 = int(input("Enter number: "))

for i in range(1, n3+1):   
    if i % 2 == 0:         
        print(i, end=" ")

#even odd seprate addition
numb = input("Enter a number: ")

totaleven = 0
totalodd = 0

for digit in numb:    
    digit = int(digit)          
    if digit % 2 == 0:  
        totaleven = totaleven + digit
    else:
        totalodd = totalodd + digit

print("even =", totaleven)
print("odd =", totalodd)

#loop
num = input('enter num or sign:')
for i in range(1,5):
   print(num*i)