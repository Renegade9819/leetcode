class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        lst = s.split()
         
        if lst:
            return len((lst[-1]))
        return 0
