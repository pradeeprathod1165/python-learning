#string operations
text = 'Python programming'

print(text[1])
print(text[-1])
print(text[0:6])
print(text.upper())
print(text.lower())
print(text.replace("Python", "Java"))
print('ing' in text)


#while loop
i = 1
while i <= 5:
    print("Count:", i)
    i += 1

#break and continue *(control loop)
for i in range(1,10):
    if i == 5:
        break
    print(i)

for j in range(1,11):
    if j == 5:
        continue
    print(j)