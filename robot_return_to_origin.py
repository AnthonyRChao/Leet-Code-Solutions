class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        countU, countD, countR, countL = 0, 0, 0, 0
        
        for move in moves:
            if move == 'U':
                countU += 1
            elif move == 'D':
                countD += 1
            elif move == 'R':
                countR += 1
            elif move == 'L':
                countL += 1
        
        if countU == countD and countR == countL:
            return True
        return False
"""
Provided Solution
class Solution(object):
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1

        return x == y == 0
        
# Even Faster One Liner Solution
class Solution(object):
    def judgeCircle(self, moves):
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

_Learnings | .count()
"""
