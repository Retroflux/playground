# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/submissions/914572383/
# Date of Submission: 2023-03-13

# Runtime: 29 ms, faster than 83.30% of Python3 online submissions for Check if One String Swap Can Make Strings Equal.
# Memory Usage: 13.7 MB, less than 96.48% of Python3 online submissions for Check if One String Swap Can Make Strings Equal.

# Problem:
#  You are given two strings s1 and s2 of equal length. A string swap is an operation where you 
#  choose two indices in a string (not necessarily different) and swap the characters at these indices.
#  Return true if it is possible to make both strings equal by performing at most one string 
#  swap on exactly one of the strings. Otherwise, return false.


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count >=3:
                    return False
        return sorted(s1) == sorted(s2)