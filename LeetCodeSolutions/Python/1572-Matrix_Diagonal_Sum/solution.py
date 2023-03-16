# https: // leetcode.com/problems/matrix-diagonal-sum/submissions/916268196/
# Date of Submission: 2023-03-16

# Runtime: 106 ms, faster than 86.57% of Python3 online submissions for Matrix Diagonal Sum.
# Memory Usage: 14 MB, less than 88.93% of Python3 online submissions for Matrix Diagonal Sum.
#

# Problem:
#  Given a square matrix mat, return the sum of the matrix diagonals.
#  Only include the sum of all the elements on the primary diagonal and 
#  all the elements on the secondary diagonal that are not part of the primary diagonal.

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sum = 0
        size = len(mat)
        for i in range(0, len(mat)):
            sum += mat[i][i]
            # don't count diagonals twice along the second axis (x = y)
            if (size-i-1 != i):
                sum += mat[size-i-1][i]
        return sum
