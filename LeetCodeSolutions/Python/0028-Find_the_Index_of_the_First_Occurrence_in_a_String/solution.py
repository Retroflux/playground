# https://leetcode.com/problems/3sum/submissions/924420848/

# Runtime: 27 ms, faster than 89.17% of Python3 online submissions for Find the Index of the First Occurrence in a String.
# Memory Usage: 13.8 MB, less than 94.84% of Python3 online submissions for Find the Index of the First Occurrence in a String.

# Problem: 
# Given two strings needle and haystack, return the index of the first occurrence of needle 
# in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(0, len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
