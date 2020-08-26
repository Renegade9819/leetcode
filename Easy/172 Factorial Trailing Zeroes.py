'''

    Take the number that you've been given the factorial of.
    Divide by 5; if you get a decimal, truncate to a whole number.
    Divide by 5^2 = 25; if you get a decimal, truncate to a whole number.
    Divide by 5^3 = 125; if you get a decimal, truncate to a whole number.
    Continue with ever-higher powers of 5, until your division results in a number less than 1. Once the division is less than 1, stop.
    Sum all the whole numbers you got in your divisions. This is the number of trailing zeroes.

'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        power = 1
        count = 0
        while(True):
            num =  n // 5**power
            power += 1
            if num < 1:
                return count
            else:
                count += num

                
                
'''
Another method

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n != 0:
            n = n // 5
            count += n
        return count
'''
