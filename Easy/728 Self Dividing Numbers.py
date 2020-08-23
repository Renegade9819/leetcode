# Naive Solution

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            if i < 10:
                result.append(i)
            elif "0" in str(i):
                continue
            else:
                num = i
                sdn = True
                while(num > 0):
                    digit = num % 10
                    num //= 10
                    if i % digit == 0:
                        continue
                    else:
                        sdn = False
                    
                if sdn == True:
                    result.append(i)
        
        return result
