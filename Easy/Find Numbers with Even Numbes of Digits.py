import math

def getDigits(num):
        if num > 0:
            digits = int(math.log10(num)) + 1
        elif n == 0:
            digits = 1
        else:
            digits = int(math.log10(-num)) + 1
        
        return digits
    
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        
        for num in nums:
            digits = getDigits(num)
            
            if(digits % 2 == 0):
                count += 1
            
        return count
