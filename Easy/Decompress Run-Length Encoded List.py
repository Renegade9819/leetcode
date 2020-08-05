class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for cnt, num in zip(nums[0::2], nums[1::2]):
            result.extend([num] * cnt)
        
        return result
