# https://leetcode.com/problems/valid-sudoku/submissions/931499187/
# Date of Submission: 2022-04-10

# Runtime: 86 ms, faster than 97.26% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 13.9 MB, less than 22.81% of Python3 online submissions for Valid Sudoku.

#Problem: Determine if a 9 x 9 Sudoku board is valid. 


#This solution was on the boards and is slightly faster than mine, but much less readable. My solution is the memoryOptimized.py version. 
class Solution:
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))


