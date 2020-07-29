lass Solution:
    def maximum69Number (self, num: int) -> int:   
        return str(num).replace('6', '9', 1)
        
        
        
'''
Same as above but more lines

class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        pos = num.find('6')
        num = num.replace(num[pos], '9', 1)
        
        return int(num)
'''

'''
Loop solution

class Solution:
    def maximum69Number (self, num: int) -> int:
        num = [int(x) for x in str(num)]
        
        for i in range(len(num)):
            if num[i] == 6:
                num[i] = 9
                break
        
        return int(''.join(map(str, num)))
'''
