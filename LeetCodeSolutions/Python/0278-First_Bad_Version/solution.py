# https://leetcode.com/problems/first-bad-version/submissions/916351535/
# Date of Submission: 2023-03-16

# Runtime: 30 ms, faster than 72.50% of Python3 online submissions for First Bad Version.
# Memory Usage: 13.7 MB, less than 95% of Python3 online submissions for First Bad Version.
#

# Problem:
#    Given two non-negative integers low and high.
#    Return the count of odd numbers between low and high (inclusive).

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # base cases for n = 1 (always return 1) and n=2 (binary search by definition)
        if n < 3:
            if n == 2 and isBadVersion(1) == False:
                return 2
            else:
                return 1

        lowerBound = 0
        found = -1
        while (1):
            # Once it's narrowed down to two, check the lower of the two to find out the answer
            if (n-lowerBound == 1):
                if (isBadVersion(lowerBound) == True):
                    return lowerBound
                else:
                    return n
            # if the middle version is bad, make that the new 'n'
            if isBadVersion(int((n + lowerBound)/2)) == True:
                n = int((n + lowerBound)/2)
            # else, everything to the left of middle is good, shift lowerBound
            else:
                lowerBound = int((lowerBound+n)/2)

#This function was a closed-box component to the solution. 
#Returns True if n >= bad version
#Returns False otherwise
def isBadVersion(n : int):
    return True
    return False