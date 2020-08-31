'''
We are given n. Let's denote the happy number operation as h(x) where x is any integer. 
If a repeated application of h(x) returns 1, we know that the number is happy.

The difficulty of this problem is to determine if a number is not happy.
One might think that h(x) always generates a unique number when compared to previous numbers. If this fact were true then every number would be happy.
This said, observe a reoccurence in for example 101:

101 -> 2 -> [4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4]

This reoccurence implies that no new unique numbers will be generated.
Given that we never saw 1, we will for certain never see it in the future.
Therefore, we can conclude that the number is not happy if a number is seen twice before seeing 1.

Note: This property is observed with any number, even if the loop in some other cases might get longer.

Thanks to alexandrelavoie on Leetcode.
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while True:
            if n in seen:
                return False
            elif n == 1:
                return True
            else:
                seen.add(n)
                n = sum([int(x) ** 2 for x in str(n)])
