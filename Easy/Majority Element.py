class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        for num, cnt in d.items():
            if cnt > len(nums) / 2:
                return num
