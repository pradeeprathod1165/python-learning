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
