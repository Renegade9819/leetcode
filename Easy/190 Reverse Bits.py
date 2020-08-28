class Solution:                 
    def reverseBits(self, n: int) -> int:
        # power 0-indexed
        ret, power = 0, 31
        
        # The input is a 32 bits signed integer.
        # We place the rightmost bit at the leftmost position by doing << power, i.e. for first loop, n << 31.
        # if the input was 00000000000000000000000000011001, after getting the rightmost bit and left shifting...
        # 00000000000000000000000000000000
        # 10000000000000000000000000000000 This happens in the first iteration. Then we decrement power by 1, so << 30
        # In the 4th iteration, the result will be 10010000000000000000000000000000
        while n:
            ret += (n & 1) << power             # n & 1 gives the rightmost bit. << left shift operator basically appends the numbers with 0s at the end.
            n = n >> 1                          # n >> 1 shifts the bit to right by 1 bit, i.e. simply removing the right bits.
            power -= 1
        
        return ret
