# By using the in-built python statistics module

import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return statistics.median(nums1 + nums2)

    
    
''' Another simple solution -
nums = sorted(nums1+nums2)
if len(nums) % 2 == 0:
    x = nums // 2
    y = (nums // 2) - 1
    return (x+y) / 2
else:
    return len(nums) // 2
'''
