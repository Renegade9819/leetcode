'''
Naive Solution

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = [paths[i][0] for i in range(len(paths))]
        result = ''
        for i in range(len(paths)):
            if paths[i][-1] not in source:
                result = paths[i][-1]
        return result
'''
