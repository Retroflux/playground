# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/913281545/
# Date of Submission: 2023-03-11

# Runtime: 27 ms, faster than 87.39% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Memory Usage: 13.8 MB, less than 92.33% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.


# Problem:
# Given an integer number n, return the difference between the 
# product of its digits and the sum of its digits.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        n = str(n)
        runningSum = 0
        runningProduct = 1

        for character in n:
                runningSum += int(character)
                runningProduct *= int(character)

        return runningProduct - runningSum
