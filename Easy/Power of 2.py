class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1073741824 % n == 0


'''
Explanation - 

In particular, n is of type int. This means it is a 4 byte, signed integer [ref]. The maximum value of this data type is 2147483647.
Knowing the limitation of n, we can now deduce that the maximum value of n that is also a power of two is 1073741824. We calculate this as:

math.log(2147483647, 2) = 30.999999999328196  
30.999999999328196  // 1 = 30

Therefore, the possible values of n where we should return true are 2^0 ... 2^30, therefore all we need to do is divide 2^30 by n. A remainder of 0 means n is a divisor of 2^30 and therefore a power of 2.

Complexity Analysis

Time complexity : O(1). We are only doing one operation.

Space complexity : O(1). We are not using any additional memory.

Solution by - Anton_Skomarovskyi
'''

'''
My Solution - 

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        
        while n % 2 == 0:
            n //= 2
        
        return n == 1
'''
