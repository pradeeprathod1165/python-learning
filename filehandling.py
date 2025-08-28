#learning file handling

#Open file
file = open('example.txt','w')

#write file
f = open("example.txt", "w")  
f.write("Hello, Python!\n")  
f.write("This is file handling step by step.")  
f.close()  

f = open("example.txt", "a")  
f.write("\nThis line is appended.")  
f.close()


#read file
f = open("example.txt", "r")  
content = f.read()  
print(content)  
f.close()

#reading methods
# f.readline()   # reads one line  
# f.readlines()  # reads all lines into a list

