#functions
def greet(name):
    print('Hello',name)

#calling function
greet('Pradeep')


#function with return values
def add(a,b):
    return (a + b)

#calling fucntions
result = add(3,5)
print(result)


#list(array in python)
fruits = ['apple','orange','graphes']

print(fruits[0])
print(len(fruits[2]))

fruits.append('watermelon')
print(fruits)

# loop through list
for fruit in fruits:
    print(fruit)


#dictionary
student = {
    'name' : 'Pradeep',
    'age' : 21,
    'is_student' : True
}

print (student['name'])
print (student['age'])

#adding new key
student['height'] = 5.4
print(student)


#nested loop
num = input('enter num or sign:')
for i in range(1,10):
   print(num*i)

#nested loop 2
rows = 5
for i in range(1, rows+1):
    for j in range(i):
        print("*", end=" ")
    print()

#pattern
rows = 5
for i in range(1, rows+1):
    for j in range(i):
        print("*", end=" ")
    print()
