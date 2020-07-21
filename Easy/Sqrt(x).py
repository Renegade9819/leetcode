class Solution:
    def mySqrt(self, x: int) -> int:
        # Using Newton's method to find the square root of x
            
        # formula - root = 1/2 * (approximation + number / approximation)
        
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            approx = 0.5 * x                  # almost any approx works, even approx = x
            root = 0.5 * (approx + x/approx)
            while root != approx:
                approx = root
                root = 0.5 * (approx + x/approx)
            return int(approx)
