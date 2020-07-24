class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        temp = numBottles
        
        while(temp >= numExchange):
            temp_q = temp // numExchange
            temp_r = temp % numExchange
            temp = temp_q + temp_r
            res += temp_q
        return res
