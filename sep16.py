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