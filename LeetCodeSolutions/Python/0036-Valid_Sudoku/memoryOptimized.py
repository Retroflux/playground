# https://leetcode.com/problems/valid-sudoku/submissions/931498690/
# Date of Submission: 2022-04-10

# Runtime: 86 ms, faster than 6.7% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 13.9 MB, less than 98.42% of Python3 online submissions for Valid Sudoku.

#Problem: Determine if a 9 x 9 Sudoku board is valid. 


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            if not self.isValidLine(board[i]):
                return False
            if not self.isValidLine(list(row[i] for row in board)):
                return False
        for i in range(0,3):
            for j in range(0,3):
                if not self.isValidSector(list(row[j*3:j*3+3] for row in board[i*3:i*3+3])):
                    return False
        return True
    
    def isValidLine(self, row):
        for i in range(1,10):
            if row.count(str(i)) > 1:
                return False
        return True

    def isValidSector(self,subBoard):
        tempList = []
        for row in subBoard:
            tempList += row
        return self.isValidLine(tempList)  