# https://leetcode.com/submissions/detail/726002324/
# Date of Submission: 2022-06-19
#
# Runtime: 30 ms, faster than 98.40% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 13.8 MB, less than 79.03% of Python3 online submissions for String to Integer (atoi).

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        negationFlag = 0
        summation = 0
        if (len(s) == 0):
            return 0

        if (s[0] == "-"):
            negationFlag = 1
            s = s[1:]
        elif (s[0] == "+"):
            s = s[1:]
        for char in s:
            if (char.isdigit()):
                summation = (summation * 10) + int(char)
            else:
                break
        if (negationFlag):
            summation *= -1
            if (summation < pow(-2, 31)):
                summation = pow(-2, 31)
        else:
            if summation > pow(2, 31) - 1:
                summation = pow(2, 31) - 1
        return summation