#list
nlist = []
n = int(input('how many number you want:'))
for i in range (n):
    num = int(input(f'enter number {i + 1}:'))
    nlist.append(num)

print (nlist) 
total = sum(nlist)
greater = max(nlist)
small = min(nlist)
print('sum:',total ,'greater number:' ,greater,'smaller number:', small)

#get grade
student = int(input('enter your percentage(e.g- 70):'))

if student >= 60 :
    print('you got a grade:A')
elif student < 60 and student >40 :
    print('you got a grade:B')
if student >=35 and student == 40 :
    print('you got a grade:c')
else:
    print('sorry you are fail and got grade:f')

#class
class Rectangle:
    def rec(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def param(self):
        return 2 * (self.length + self.width)


s = Rectangle()
s.rec(5, 3)  
print("Area:", s.area())
print("Perimeter:", s.param())

#class and object car
class car:
    def cardetail(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def toyota(self):
        self.brand = 'toyota'
        self.model = 'T1104'
        print(f'enginer start for car brand {self.brand} and model is {self.model}')

    def BMW(self):
        self.brand = 'BMW'
        self.model = 'B04'
        print(f'enginer start for car brand {self.brand} and model is {self.model}')

s = car()
s.toyota()
s.BMW()