# https: // leetcode.com/problems/subtract-the-product-and -sum-of-digits-of-an-integer/submissions/913278995/
# Date of Submission: 2023-03-11

# Runtime: 31 ms, faster than 67.62% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Memory Usage: 13.8 MB, less than 42.35% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.


# Problem:
# Given an integer number n, return the difference between the
# product of its digits and the sum of its digits.


class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        runningSum = 0
        runningProduct = 1

        while n > 0:
            runningSum += n % 10
            runningProduct *= n % 10

            n = int(n/10)
            print(n)
        return runningProduct - runningSum
