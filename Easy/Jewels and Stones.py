class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = collections.Counter(S)
        result = 0
        for j in J:
            if jewels and j in jewels:
                result += jewels[j]
        return result
