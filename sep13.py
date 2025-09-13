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
n = int(input("Enter integer: "))
last = abs(n) % 10
print("Last digit:", last)
