class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # comb is used for calculating Binomial Coefficient
        return [[int(comb(x, y)) for y in range(x + 1)] for x in range(numRows)]
    
        '''
        Used the formula from - 
        https://mathworld.wolfram.com/PascalsTriangle.html
        
        and
        
        https://www.mathsisfun.com/pascals-triangle.html
