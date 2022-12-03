# https://leetcode.com/submissions/detail/721625743/
# Date of Submission: 2022-06-13

# Runtime: 87 ms, faster than 62.00% of Python3 online submissions for Triangle.
# Memory Usage: 14.7 MB, less than 99.00% of Python3 online submissions for Triangle.


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        currRow = 1

        # base cases
        if (len(triangle) == 1):
            return triangle[0][0]
        elif (len(triangle) == 2):
            return triangle[0][0] + min(triangle[1][0], triangle[1][1])

        # loop through and greedy lowest sum each column
        while (len(triangle) > 1):
            for i in range(1, currRow):
                triangle[1][i] += min(triangle[0][i - 1], triangle[0][i])
            triangle[1][0] += triangle[0][0]  # left edge case
            triangle[1][currRow] += triangle[0][currRow - 1]  # right edge case
            # reduce triangle
            currRow += 1
            triangle = triangle[1:]
        return min(triangle[0])  # triangle is now only 1 row tall, take min of that row


def getLeftEdgeSum(triangle) -> int:
    sum = 0
    for i in range(0, len(triangle)):
        sum += triangle[i][0]
    return sum


def getRightEdgeSum(triangle) -> int:
    sum = 0
    for i in range(0, len(triangle)):
        sum += triangle[i][i]
    return sum
