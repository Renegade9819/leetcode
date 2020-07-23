'''
Binary Search method.
Compute mid, if the mid is the bad version, then reduce the search scope right = mid - 1, since mid might not be the first bad version,
and we are sure that every version after mid will be a bad version.
if mid is not the bad version, then we search starting from left = mid + 1.
At one point Left > Right and the loop will break, and Left will always be the first bad version. 
http://www.cs.cornell.edu/courses/cs211/2006sp/Lectures/L06-Induction/binary_search.html
'''


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1): return 1
        
        left = 1
        right = n
        while(left <= right):
            mid = left + (right - left) // 2
            if(isBadVersion(mid)):
                right = mid -1
            else:
                left = mid + 1
        return left
