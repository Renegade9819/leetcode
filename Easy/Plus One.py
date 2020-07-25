# Iterative solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] <= 8:
            digits[-1] += 1
            return digits
        else:
            for i in range(len(digits)-1, -1, -1):
                if digits[i] != 9:
                    i += 1
                    break
                else:
                    digits[i] = 0
                    
            if i != 0:
                digits[i-1] += 1
                return digits
            else:
                digits[0] = 1
                digits.append(0)
                return digits



''' Recursive solution

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] <= 8:
            digits[-1] += 1
            return digits
        elif len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        else:
            digits[-1] = 0
            digits[0:-1] = self.plusOne(digits[0:-1])
            return digits
'''
