# https://leetcode.com/problems/is-subsequence/submissions/913318967/
# Date of Submission: 2023-03-11

# Runtime: 32 ms, faster than 73.69% of Python3 online submissions for Is Subsequence.
# Memory Usage: 13.9 MB, less than 71.18% of Python3 online submissions for Is Subsequence.

#Problem:
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by 
# deleting some (can be none) of the characters without disturbing the relative positions 
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        currPos = 0
        if s in t:
            return True

        for char in t:
            if (currPos == len(s)):
                return True
            if (s[currPos] == char):
                currPos += 1
        if (currPos == len(s)):
            return True
        return False
