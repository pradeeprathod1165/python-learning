name = "Pradeep"
age = 21
print(f'Your name is {name}, and ypur age is {age}')

#Check if a number is positive or negative
num = int(input("Enter a number: "))
if num %2 == 0:
    print('even')
else :
    print('odd')

#Print numbers from 1 to 10.
for i in range(1,11):
    print(i)

#Print only even numbers from 1 to 20.
for i in range(2,21,2):
    print(i)

#Print multiplication table of 5.
for i in range(5,55,5):
    print(i)

#Write a function to return the square of a number.
def squarenum(n):
    return n*n
   
n =int(input('enter number:'))
print('square is',squarenum(n))
