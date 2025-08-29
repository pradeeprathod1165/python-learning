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

# with 
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())


#checking file is exist or not

import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File not found")


#deleting
import os

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("File deleted successfully")
else:
    print("No file found")


#copy image
# with open("image.jpg", "rb") as f:     # read binary
#     data = f.read()

# with open("copy.jpg", "wb") as f:      # write binary
#     f.write(data)

#working with directories
import os

# create a folder named "myfolder"
os.mkdir("myfolder")

print("Folder created successfully")
