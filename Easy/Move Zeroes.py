class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key = lambda num: num == 0)



'''
Another method
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = nums.count(0)
        
        for i in range(cnt):
            nums.remove(0)
            nums.append(0)
'''
