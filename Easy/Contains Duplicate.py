class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True


'''
Solution - 2

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsOriginal = set()
        numsDuplicate = set()
        nums_add = numsOriginal.add
        numsDuplicate_add = numsDuplicate.add
        
        for num in nums:
            if num in numsOriginal:
                numsDuplicate_add(num)
            else:
                nums_add(num)
        
        if (len(numsDuplicate) > 0):
            return True
        return False
'''

'''
Solution - 3

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        seen_add = seen.add
        seen_twice = set(x for x in nums if x in seen or seen_add(x))
        
        if len(seen_twice) > 0:
            return True
        return False
'''

'''
Solution - 4

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num in hashmap: return True
            else: hashmap[num] = 1
        return False
'''
        
