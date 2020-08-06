class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        res = 0
        for k, v in count.items():
            res += v * (v - 1) // 2
        return res
