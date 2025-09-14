#grade calculator
sub1 = int(input('Enter mark sub1:'))
sub2 = int(input('Enter mark sub2:'))
sub3 = int(input('Enter mark sub3:'))

#average 
sum = sub1 + sub2 + sub3 
average = (sum / 3)
print(average)

#grade calculation
if average >= 75:
    print('Grade A')
elif average >=50 :
    print('Grade B')
else:
    print('Grade C')


#Last digit finder
num = (input('enter number:'))

print(num[-1])

#last digit finder method 2
s = input("Enter a number: ")
n = int(float(s))   # convert to float first, then to int
last = abs(n) % 10
print("Last digit:", last)


#check divisibility
num2 = int(input('enter your number:'))

if num2 / 3 and num2/5:
    print('number is divisble by 3 and 5')
else:
    print('not divisible')
 

 #bill splitter
bill = int(input('enter bill amount:'))
people = int(input('enter number of people:'))

#bill splitting
split = bill / people

print('split amount is :',split)

#greatest of three number
n1 = int(input('enter first number:'))
n2 = int(input('enter second number:'))
n3 = int(input('enter third number:'))

if n1 > n2 and n1 > n3:
    print('number 1 greater:',n1)
elif n2 > n1 and n2 > n3:
    print('num 2 is greater:',n2)
else:
    print('num 3 is greater:',n3)

#sum of digit
numb = input("Enter a number: ")

total = 0
for digit in numb:       
    total = total + int(digit)

print("Sum of digits =", total)

#reverse
numb1 = input('enter number')
print('rever',numb1[::-1])