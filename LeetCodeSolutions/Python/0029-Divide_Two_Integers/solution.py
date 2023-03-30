# https://leetcode.com/problems/divide-two-integers/submissions/925007472/

# Runtime: 30 ms, faster than 87.54% of Python3 online submissions for Divide Two Integers.
# Memory Usage: 13.8 MB, less than 97.9% of Python3 online submissions for Divide Two Integers.

# Problem:
# Given two integers dividend and divisor, divide two integers without using 
# multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing 
# its fractional part. For example, 8.345 would be truncated to 8, and 
# -2.7335 would be truncated to - 2.
# Return the quotient after dividing dividend by divisor.

class Solution:
    def divide(self, A, B):
        if (A == -2147483648 and B == -1):
            return 2147483647
        a, b, res = abs(A), abs(B), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (A > 0) == (B > 0) else -res

    # BRO this works, but the only way to make it work is to break
    # the rules of the problem and use exponential bit shifting... which is fancy multiplication.
    # This problem is ridiculous.

    # def divide(self, dividend: int, divisor: int) -> int:
    #     count = 0
    #     differenceInSigns = 1

    #     if dividend == divisor:
    #         return 1

    #     if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
    #         differenceInSigns = -1

    #     dividend = abs(dividend)
    #     divisor = abs(divisor)

    #     if divisor == 1:
    #         if differenceInSigns == 1 and dividend >= (2**31)-1:
    #             return differenceInSigns * ((2**31)-1)
    #         elif differenceInSigns == -1 and dividend <= -(2**31):
    #             return differenceInSigns * (2**31)
    #         return differenceInSigns * dividend

    #     while dividend >= divisor:
    #         dividend -= divisor
    #         count+=1

    #     # if count >= 2**31-1:
    #     #     return differenceInSigns * (2**31)-1


    #     return differenceInSigns * count
Console
