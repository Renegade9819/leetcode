class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        a_mis_loc = []
        
        for i in range(len(A)):
            if A[i] != B[i]:
                a_mis_loc.append(i)            
                
                
        if len(a_mis_loc) == 2:        
            A = list(A)
            A[a_mis_loc[0]], A[a_mis_loc[1]] = A[a_mis_loc[1]], A[a_mis_loc[0]]
            A = ''.join(A)
            if A == B:
                return True
        elif len(a_mis_loc) == 0 and A == B and len(A) > len(set(A)):
            return True
        else:
            return False
