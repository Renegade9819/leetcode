class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
            
        for i in range(num):
            if num % 2 == 0:
                num //= 2
            elif num % 2 != 0:
                num -= 1
                if num == 0:
                    return i+1
