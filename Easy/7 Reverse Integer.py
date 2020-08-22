class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        
        signbit = 1 if x < 0 else 0
        
        x = abs(x)
        while (x > 0):
            rev = (rev*10) + (x % 10)
            x = x // 10
        
        if (rev > 1<<31):
            return 0
        
        if (signbit == 1):
            return -rev
        else:
            return rev
