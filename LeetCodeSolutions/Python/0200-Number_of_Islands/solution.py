# https://leetcode.com/problems/number-of-islands/submissions/917624967/

# Runtime: 288 ms, faster than 83.8% of Python3 online submissions for Number of Islands.
# Memory Usage: 16.3 MB, less than 80.23% of Python3 online submissions for Nuomber of Islands.
#
# Problem:
#  Given an m x n 2D binary grid grid which represents a map 
#  of '1's (land) and '0's (water), return the number of islands.
#
#  An island is surrounded by water and is formed by connecting 
#  adjacent lands horizontally or vertically. You may assume all 
#  four edges of the grid are all surrounded by water.


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_y = len(grid)
        max_x = len(grid[0])

        numIslands = 0

        for i in range(0, max_y):
            for j in range(0, max_x):
                if grid[i][j] == "1":
                    numIslands += 1
                    grid = floodIsland(grid, i, j, max_y, max_x)
        return numIslands

#Atlantis that island so you can't check it again
def floodIsland(grid, i, j, max_y, max_x):
    if isValidDirection(i, j-1, max_y, max_x) and grid[i][j-1] == "1":
        grid[i][j-1] = "0"
        grid = floodIsland(grid, i, j-1, max_y, max_x)
    if isValidDirection(i, j+1, max_y, max_x) and grid[i][j+1] == "1":
        grid[i][j+1] = "0"
        grid = floodIsland(grid, i, j+1, max_y, max_x)
    if isValidDirection(i-1, j, max_y, max_x) and grid[i-1][j] == "1":
        grid[i-1][j] = "0"
        grid = floodIsland(grid, i-1, j, max_y, max_x)
    if isValidDirection(i+1, j, max_y, max_x) and grid[i+1][j] == "1":
        grid[i+1][j] = "0"
        grid = floodIsland(grid, i+1, j, max_y, max_x)

    return grid


def isValidDirection(y, x, max_y, max_x) -> bool:
    if x >= 0 and y >= 0 and x < max_x and y < max_y:
        return True
    return False
