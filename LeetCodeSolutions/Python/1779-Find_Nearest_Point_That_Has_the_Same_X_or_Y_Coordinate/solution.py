# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/submissions/913903133/
# Date of Submission: 2023-03-12

# Runtime: 717 ms, faster than 75.33% of Python3 online submissions for Find Nearest Point That Has the Same X or Y Coordinate.
# Memory Usage: 19.3 MB, less than 30.68% of Python3 online submissions for Find Nearest Point That Has the Same X or Y Coordinate.
#

# Problem:
# You are given two integers, x and y, which represent your current location on a 
# Cartesian grid: (x, y). You are also given an array points where each 
# points[i] = [ai, bi] represents that a point exists at (ai, bi). 
# 
# A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

# Return the index(0-indexed) of the valid point with the smallest Manhattan distance 
# from your current location. If there are multiple, return the valid point with the 
# smallest index. If there are no valid points, return -1.

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        closestDistance = 99999
        index = -1

        for i in range(0, len(points)):
            if points[i][0] == x or points[i][1] == y:
                manhattanDistance = calculateManhattanDistance(
                    x, points[i][0],
                    y, points[i][1])

                if manhattanDistance < closestDistance:
                    index = i
                    closestDistance = manhattanDistance
        return index


def calculateManhattanDistance(x1, x2, y1, y2):
    return abs(x1-x2) + abs(y1-y2)
