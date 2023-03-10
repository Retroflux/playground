# https://leetcode.com/problems/number-of-1-bits/submissions/912820094/
# Date of Submission: 2023-03-10

# Runtime: 34 ms, faster than 57.7% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 13.8 MB, less than 91.3% of Python3 online submissions for Number of 1 Bits.

# Problem:
#Write a function that takes the binary representation of an 
# unsigned integer and returns the number of '1' bits it has
# (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        n = str(bin(n))

        for bit in n:
            if bit == '1':
                count += 1
        return count
