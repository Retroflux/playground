# https://leetcode.com/problems/isomorphic-strings/submissions/913303291/
# Date of Submission: 2023-03-11

# Runtime: 35 ms, faster than 72% of Python3 online submissions for Happy Number.
# Memory Usage: 13.7 MB, less than 94.97% of Python3 online submissions for Happy Number.

# Problem:
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:
#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#     Those numbers for which this process ends in 1 are happy.
#     Return true if n is a happy number, and false if not.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # build dict of pairings, where s[i] is the key and t[i] is value

        # if key:value exists, continue;
        # however if key:notValue exists, return False
        # however if notKey:Value exists, return False
        # return True if you can create the dict without errors.

        isometricPairs = dict()

        for i in range(0, len(s)):
            if s[i] in isometricPairs and t[i] == isometricPairs[s[i]]:
                continue
            elif s[i] in isometricPairs and t[i] != isometricPairs[s[i]]:
                return False
            elif t[i] in isometricPairs.values() and s[i] not in isometricPairs:
                return False
            else:
                isometricPairs[s[i]] = t[i]

        return True
