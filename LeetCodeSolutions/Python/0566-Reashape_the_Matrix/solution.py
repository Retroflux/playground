# https: // leetcode.com/problems/reshape-the-matrix/submissions/916293575/
# Date of Submission: 2023-03-16

# Runtime: 82 ms, faster than 96.46% of Python3 online submissions for Reshape the Matrix.
# Memory Usage: 14.7 MB, less than 70.50% of Python3 online submissions for Reshape the Matrix.

#Problem:
# You are given an m x n matrix mat and two integers r and c representing the number of 
# rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the 
# same row-traversing order as they were.

# If the reshape operation with given parameters is possible 
# and legal, output the new reshaped matrix
# Otherwise, output the original matrix.

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        # ensure it's not the same matrix or an impossible matrix
        if len(mat) == r and len(mat[0]) == c:
            return mat
        elif len(mat)*len(mat[0]) != r*c:
            return mat

        # serialize data into single row; could be optimized into in-place formula
        tempList = list()
        for row in mat:
            tempList += row

        # create new matrix based off r,c
        newMat = list()
        for i in range(0, r*c, c):
            newMat.append(tempList[i:i+c])

        return newMat