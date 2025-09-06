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