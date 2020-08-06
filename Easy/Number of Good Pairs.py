class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        res = 0
        for k, v in count.items():
            res += v * (v - 1) // 2
        return res


'''
Another simple solution

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        hashMap = {}
        res = 0
   
        for number in nums:            
            if number in hashMap:
                res += hashMap[number]
                hashMap[number] += 1
            else:
                hashMap[number] = 1
                
        return res
'''
