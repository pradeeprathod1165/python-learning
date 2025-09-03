name ='Pradeep'
age = 21
height = 5.4
is_student = True
print(name,age,height,is_student)
print (type(name),type(age),type(height),type(is_student))


#input output
num1 = input('enter number 1:')
num2 = input('enter number 2:')
num3 = int(num1)
num4 = int(num2)

#operations
print(num3 + num4)
print(num3 - num4)
print(num3 * num4)
print(num3 / num4)
print(num3 // num4)
print(num3 ** num4)
print(num3 % num4)


#program : age verification
age1 = int(input('enter your age:'))
if age1 >= 18:
    print('you are eligible')
else :
    print('you are not eligible')

#program 2 : number verification
usernum = int(input('Enter your number:'))
if usernum % 2 == 0:
    print('positive,even')
else:
    print('negative,odd')

# 1 to 20
for i in range(1,20):
   if i % 2 == 0:
    print(i)

#pattern
num = input('enter num:')
for i in range(1,10):
   print(num*i)
