# https://leetcode.com/problems/number-of-enclaves/submissions/929335573/
# Date of Submission: 2023-04-06

# Runtime: 634 ms, faster than 85.77% of Python3 online submissions for Number of Enclaves.
# Memory Usage: 15.5 MB, less than 94.11% of Python3 online submissions for Number of Enclaves.

# Problem:
#  You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
#  A move consists of walking from one land cell to another adjacent(4-directionally) 
#  land cell or walking off the boundary of the grid.
# 
#  Return the number of land cells in grid for which we cannot walk off
#  the boundary of the grid in any number of moves.

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        edgeLocations = self.buildOuterList(grid)
        totalOuter = len(edgeLocations)
        while len(edgeLocations) > 0:
            edgeLocations = self.checkOrdinalSpace(grid, edgeLocations)
        return self.countRemainingOnes(grid)

    def buildOuterList(self, grid) -> list:
        edgeLocations = list()
        n = len(grid)
        m = len(grid[0])
        for i in range(0, m):
            if grid[0][i] == 1:
                edgeLocations.append((0, i))
                grid[0][i] = 0
            if grid[n-1][i] == 1:
                edgeLocations.append((n-1, i))
                grid[n-1][i] = 0
        for i in range(1, n-1):
            if grid[i][0] == 1:
                edgeLocations.append((i, 0))
                grid[i][0] = 0
            if grid[i][m-1] == 1:
                edgeLocations.append((i, m-1))
                grid[i][m-1] = 0
        print(edgeLocations)
        return edgeLocations

    def checkOrdinalSpace(self, grid, edgeLocations) -> list:
        m = len(grid)
        n = len(grid[0])
        count = 0
        newList = list()

        for cell in edgeLocations:
            if self.checkValidDirection(m, n, cell[0]-1, cell[1]):
                if grid[cell[0]-1][cell[1]] == 1:
                    newList.append((cell[0]-1, cell[1]))
                    grid[cell[0]-1][cell[1]] = 0
            if self.checkValidDirection(m, n, cell[0]+1, cell[1]):
                if grid[cell[0]+1][cell[1]] == 1:
                    newList.append((cell[0]+1, cell[1]))
                    grid[cell[0]+1][cell[1]] = 0
            if self.checkValidDirection(m, n, cell[0], cell[1]-1):
                if grid[cell[0]][cell[1]-1] == 1:
                    newList.append((cell[0], cell[1]-1))
                    grid[cell[0]][cell[1]-1] = 0
            if self.checkValidDirection(m, n, cell[0], cell[1]+1):
                if grid[cell[0]][cell[1]+1] == 1:
                    newList.append((cell[0], cell[1]+1))
                    grid[cell[0]][cell[1]+1] = 0
            grid[cell[0]][cell[1]] = 0

        return newList

    def checkValidDirection(self, m, n, newM, newN) -> bool:
        if newM < 0 or newN < 0:
            return False
        elif newM >= m:
            return False
        elif newN >= n:
            return False
        return True

    def countRemainingOnes(self, grid) -> int:
        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
        return count
