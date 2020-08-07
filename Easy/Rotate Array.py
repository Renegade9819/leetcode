# List Slicing Solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]

'''
Reverse array solution

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())        # This consumes a lot of time.
'''
