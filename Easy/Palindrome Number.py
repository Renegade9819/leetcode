class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        y = x
        
        signbit = 1 if x < 0 else 0
        if (signbit == 1):
            return False
        else:
            while(x > 0):
                a = x % 10
                rev = (rev * 10) + a
                x = x // 10
            
            # check if the integer overflowed while reversing
            if (rev > 1<<31):
                return False
            if (y == rev):
                return True
            else:
                return False
