class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper() == True and word[1:].islower() == True:
            return True
        elif word[:].islower() == True:
            return True
        elif word[:].isupper() == True:
            return True
        else:
            return False
            
'''
Alternative one liner solution -
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
'''
