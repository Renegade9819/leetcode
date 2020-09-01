# Solution - 2
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')



'''
Solution - 1

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        set_bits = 0
        
        while num > 0:
            set_bits += num & 1
            num >>= 1
        
        return set_bits
'''
