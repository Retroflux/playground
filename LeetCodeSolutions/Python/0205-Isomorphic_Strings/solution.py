# https://leetcode.com/problems/isomorphic-strings/submissions/913303291/
# Date of Submission: 2023-03-11

# Runtime: 36 ms, faster than 88.36% of Python3 online submissions for Isomorphic Strings.
# Memory Usage: 14.1 MB, less than 81.48% of Python3 online submissions for Isomorphic Strings.

# Problem:
#  Given two strings s and t, determine if they are isomorphic.
#  Two strings s and t are isomorphic if the characters in s can be replaced to get t.

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
