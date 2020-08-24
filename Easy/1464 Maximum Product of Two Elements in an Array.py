# Solution 1

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lst = heapq.nlargest(2, nums)
        return (lst[0] - 1) * (lst[1] - 1)

'''
Solution - 2

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxNum_1 = max(nums)
        nums.remove(maxNum_1)
        maxNum_2 = max(nums)
        return (maxNum_1 - 1) * (maxNum_2 - 1)
'''

'''
Solution - 3

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num1 = num2 = float('-inf')
        
        for x in nums:
            if x > num2:
                if x >= num1:
                    num1, num2 = x, num1
                else:
                    num2 = x
        
        return (num1 - 1) * (num2 - 1)
'''

'''
Solution - 4

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
'''
