'''
Explanation

The trick is super simple, you XOR the 6th bit (or 5th depending on how you count bits) and that changes the case.

Example ->
a = 01100001
A = 01000001

Another trick is if you XOR a character with a whitespace, the case of the character changes.
Example -> 'A' ^ ' ' = 'a' OR 'a' ^ ' ' = 'A'

The range of ASCII characters A-Z is 65-90 in Decimal.
'''

class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ''
        space = ord(' ')
        for letter in str:
            if ord(letter) in range(65,91):
                res += chr(ord(letter) ^ space)
            else:
                res += letter
        return res
