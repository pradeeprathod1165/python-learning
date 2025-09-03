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


#program 
age1 = int(input('enter your age:'))
if age1 >= 18:
    print('you are eligible')
else :
    print('you are not eligible')