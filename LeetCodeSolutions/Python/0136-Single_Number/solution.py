# https://leetcode.com/problems/single-number/submissions/928711871/
# Date of Submission: 2023-04-05

# Runtime: 130 ms, faster than 84.57% of Python3 online submissions for Single Number.
# Memory Usage: 16.7 MB, less than 82.67% of Python3 online submissions for Single Number.

# Problem:

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (functools.reduce(operator.ixor, nums))