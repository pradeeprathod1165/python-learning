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
 