class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsSorted = sorted(nums)
        myCounter = {}
        for i, num in enumerate(numsSorted):
            if num not in myCounter:
                myCounter[num] = i
        return [myCounter[num] for num in nums]


'''
Inefficient Solution

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsSorted = sorted(nums, reverse=True)
        d = collections.Counter(numsSorted)
        result = []
        len_ = len(nums)
        for i in range(0, len_):
            temp = numsSorted.index(nums[i])
            if all(numsSorted[temp] == ele for ele in numsSorted[temp:]):
                result.append(0)
            elif d[numsSorted[temp]] > 1:
                result.append((len_ - 1) - temp - (d[numsSorted[temp]] - 1))
            else:
                result.append((len_ - 1) - temp)
                
        return result
'''
