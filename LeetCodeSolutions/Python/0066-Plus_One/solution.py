# https://leetcode.com/submissions/detail/749740658/
# Date of Submission: 2022-07-17

# Runtime: 31 ms, faster than 96.33% of Python3 online submissions for Plus One.
# Memory Usage: 13.9 MB, less than 58.40% of Python3 online submissions for Plus One.


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        currPos = len(digits) - 1

        while (currPos > 0):
            if (digits[currPos] < 9):
                digits[currPos] += 1
                return digits
            digits[currPos] = 0
            currPos -= 1

        digits[0] += 1
        if (digits[0] >= 10):
            digits[0] = 0
            digits.insert(0, 1)
        return digits
