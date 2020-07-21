class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        
        # Rabin-Karp algorithm, thanks to -> https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
        
        n = len(haystack)
        m = len(needle)
        
        hsNeedle = hash(needle)
        
        for i in range(n-m+1):
            if hash(haystack[i:i+m]) == hsNeedle:
                return i
        return -1
        
'''
Simple python solution

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        
        index = -1
        if needle in haystack:
            index = haystack.find(needle)
        return index
'''
