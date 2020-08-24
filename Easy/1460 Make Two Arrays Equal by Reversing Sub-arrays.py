class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if Counter(target) == Counter(arr):                           # OR sorted(target) == sorted(arr)   ### This is slower because its sorting the arrays.
            return True
        return False
