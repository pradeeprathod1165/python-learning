#list 
#creating list
fruits = ["apple", "banana", "mango"]
nums   = [10, 20, 30, 40]

#accessing elements
print(fruits[0])      
print(nums[-1])  

#length of element
print(len(nums))  

#changing element
nums[1] = 25 

# loop through list (for each element)
for x in nums:
    print(x)

# loop using index
for i in range(len(nums)):
    print("index", i, "value", nums[i])

#list operations
lst = [3, 1, 4]

# add
lst.append(5)       
lst.insert(1, 9)

# remove
lst.remove(9)         
last = lst.pop() 

# built-in helpers
print(sum(lst))      
print(max(lst), min(lst))

# count occurrences
print(lst.count(1))

# sort & reverse
lst.sort()            
lst.reverse()   

#sum of all in list
parts = input("Enter numbers: ").split()
total = 0
for p in parts:
    total += int(p)
print("Sum =", total)
