class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[length] = nums[i]
                length += 1
        return length
        
        
        
'''
This doesn't actually remove all the duplicates from the array.
Example - input list = [1,1,2,2,3,4,4,5]

the function only places unique elements at their proper places, 
and returns the length upto the last unique element.

leetcode accepts this answer because it only wants the length of the array
uptil the last unique element.

In reality, the array after the calculation becomes 1, 2, 3, 4, 5, 4, 4, 5],
which is not technically the correct answer.
'''
