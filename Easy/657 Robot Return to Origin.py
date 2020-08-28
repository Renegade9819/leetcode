# Solution - 2

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move = Counter(moves)
        if move['U'] == move['D'] and move['L'] == move['R']:
            return True
        return False


'''
Solution - 1

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        resultVerticle = 0
        resultHorizontal = 0
        
        for move in moves:
            if move == 'U':
                resultVerticle += 1
            elif move == 'D':
                resultVerticle -= 1
            elif move == 'L':
                resultHorizontal += 1
            elif move == 'R':
                resultHorizontal -= 1
            else:
                continue
        
        if resultVerticle == 0 and resultHorizontal == 0:
            return True
        return False
'''
