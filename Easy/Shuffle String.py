class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        len_ = len(s)
        res = [''] * len_
        for i in range(len_):
            res[indices[i]] = s[i]
        
        return ''.join(res)
