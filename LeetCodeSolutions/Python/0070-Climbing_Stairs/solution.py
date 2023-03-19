# https://leetcode.com/problems/climbing-stairs/submissions/918225859

# Runtime: 27 ms, faster than 87.42% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.8 MB, less than 93.73% of Python3 online submissions for Climbing Stairs.
#

# Problem:
#  You are climbing a staircase. It takes n steps to reach the top.
#  Each time you can either climb 1 or 2 steps. In how many 
#  distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:

        # base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # setup
        firstNumber = 1
        secondNumber = 2
        combination = 2

        for i in range(2, n):
            combination = secondNumber + firstNumber
            firstNumber = secondNumber
            secondNumber = combination

        return combination
