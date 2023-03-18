# https://leetcode.com/problems/flood-fill/submissions/917611227/

# Runtime: 62 ms, faster than 99.76% of Python3 online submissions for Flood Fill.
# Memory Usage: 14 MB, less than 85.20% of Python3 online submissions for Flood Fill.
#
# Problem:
# An image is represented by an m x n integer grid image where image[i][j] 
# represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform 
# a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels 
# connected 4-directionally to the starting pixel of the same color as 
# the starting pixel, plus any pixels connected 4-directionally to those 
# pixels(also with the same color), and so on. Replace the color of all of 
# the aforementioned pixels with color.

# Return the modified image after performing the flood fill.


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        max_y = len(image)
        max_x = len(image[0])
        target = image[sr][sc]

        if target == color:
            return image

        image[sr][sc] = color
        image = recursivePaint(image, sr, sc, max_y, max_x, target, color)
        return image


def recursivePaint(image, sr, sc, max_y, max_x, target, color):
    if isValidDirection(sr, sc-1, max_x, max_y) and image[sr][sc-1] == target:
        image[sr][sc-1] = color
        image = recursivePaint(image, sr, sc-1, max_y, max_x, target, color)

    if isValidDirection(sr, sc+1, max_x, max_y) and image[sr][sc+1] == target:
        image[sr][sc+1] = color
        image = recursivePaint(image, sr, sc+1, max_y, max_x, target, color)

    if isValidDirection(sr-1, sc, max_x, max_y) and image[sr-1][sc] == target:
        image[sr-1][sc] = color
        image = recursivePaint(image, sr-1, sc, max_y, max_x, target, color)

    if isValidDirection(sr+1, sc, max_x, max_y) and image[sr+1][sc] == target:
        image[sr+1][sc] = color
        image = recursivePaint(image, sr+1, sc, max_y, max_x, target, color)
    return image


def isValidDirection(y, x, max_x, max_y) -> bool:
    if x >= 0 and y >= 0 and x < max_x and y < max_y:
        return True
    return False
