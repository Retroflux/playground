# https://leetcode.com/problems/fibonacci-number/submissions/918203319

# Runtime: 27 ms, faster than 90.99% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.9 MB, less than 42.35% of Python3 online submissions for Fibonacci Number.
#

# Problem:
#  The Fibonacci numbers, commonly denoted F(n) form a sequence,
#  called the Fibonacci sequence, such that each number is the 
#  sum of the two preceding ones, starting from 0 and 1. That is,

class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1:
            return 1

        firstNumber = 1
        secondNumber = 1
        newNumber = 1
        for i in range(2, n):
            newNumber = firstNumber + secondNumber
            firstNumber = secondNumber
            secondNumber = newNumber
        return newNumber
