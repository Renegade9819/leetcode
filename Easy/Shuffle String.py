class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        len_ = len(s)
        res = [''] * len_
        for i, letter in zip(range(len_), range(len_)):
            res[indices[i]] = s[letter]
        
        return ''.join(res)
