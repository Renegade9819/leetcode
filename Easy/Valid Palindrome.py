import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        pattern = re.compile('[\W_]+')    # Remove everything except alphanumeric characters
        s = pattern.sub('', s)
        s = s.lower()
        if s == s[::-1]:
            return True
        else:
            return False
