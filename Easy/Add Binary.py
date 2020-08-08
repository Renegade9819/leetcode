# Solution 2
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]




'''
Solution - 1

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxLen = max(len(a), len(b))
        
        a = a.zfill(maxLen)
        b = b.zfill(maxLen)
        
        result = ''
        carry = 0
        
        i = maxLen - 1
        
        while(i >= 0):
            add = int(a[i]) + int(b[i])
            if add == 2:                                # 1 + 1
                if carry == 0:
                    carry = 1
                    result = "%s%s" % (result, '0')
                else:
                    result = "%s%s" % (result, '1')
            elif add == 1:                              # 1 + 0
                if carry == 1:
                    result = "%s%s" % (result, '0')
                else:
                    result = "%s%s" % (result, '1')
            else:                                       # 0 + 0
                if carry == 1:
                    result = "%s%s" % (result, '1')
                    carry = 0
                else:
                    result = "%s%s" % (result, '0')
            
            i -= 1
            
        if carry > 0:
            result = "%s%s" % (result, '1')
        
        return result[::-1]
'''
