# https://leetcode.com/submissions/detail/749749571/
# Date of Submission: 2022-07-17

# Runtime: 54 ms, faster than 46.92% of Python3 online submissions for Add Binary.
# Memory Usage: 13.9 MB, less than 72.46% of Python3 online submissions for Add Binary.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aPlusB = convertToDecimal(a) + convertToDecimal(b)

        outString = ""
        largestPow = 0

        while (pow(2, largestPow + 1) <= aPlusB):
            largestPow += 1

        while (largestPow >= 0):
            if (pow(2, largestPow) <= aPlusB):
                outString += "1"
                aPlusB -= pow(2, largestPow)
            else:
                outString += "0"
            largestPow -= 1

        return outString


def convertToDecimal(a: str) -> int:
    currPos = len(a) - 1
    powerMultiplier = 0
    decSum = 0

    while (currPos > -1):
        decSum += int(a[currPos]) * int(pow(2, powerMultiplier))
        currPos -= 1
        powerMultiplier += 1
    return decSum
