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