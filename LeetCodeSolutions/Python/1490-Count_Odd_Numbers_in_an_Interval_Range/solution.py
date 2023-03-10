# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/submissions/912795009/
# Date of Submission: 2023-03-10

# Runtime: 28 ms, faster than 81.77% of Python3 online submissions for Count Odd Numbers in an Interval Range.
# Memory Usage: 13.8 MB, less than 48.62% of Python3 online submissions for Count Odd Numbers in an Interval Range.
#

# Problem:
#    Given two non-negative integers low and high.
#    Return the count of odd numbers between low and high (inclusive).

from math import ceil, floor

class Solution:
    def countOdds(self, low: int, high: int) -> int:

        # one liner to solve the issue in O(1) time
        return int(ceil((low % 2 + high % 2)/2) + floor(high - low)/2)
