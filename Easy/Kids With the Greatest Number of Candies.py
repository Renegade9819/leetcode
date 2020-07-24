class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatestCandy = max(candies)
        return [(i + extraCandies) >= greatestCandy for i in candies]
