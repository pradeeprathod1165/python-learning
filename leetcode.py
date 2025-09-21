#9 - palindrome
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

       
        s = str(x)
        return s == s[::-1]


#412. Fizz Buzz
class Solution:
    def fizzBuzz(self, n: int):
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
    
#1 -two sum
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                 return [i,j]
