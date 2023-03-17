# https: // leetcode.com/problems/merge-strings-alternately/submissions/916882031/
# Date of Submission: 2023-03-17

# Runtime: 31 ms, faster than 74.83% of Python3 online submissions for Merge Strings Alternately.
# Memory Usage: 13.7 MB, less than 96.79% of Python3 online submissions for Merge Strings Alternately.
#
# Problem:
# You are given two strings word1 and word2. Merge the strings by adding letters in 
# alternating order, starting with word1. If a string is longer than the other, append 
# the additional letters onto the end of the merged string. Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        shortestStringLen = min(len(word1), len(word2))
        outString = ""

        for i in range(0, shortestStringLen):
            outString += word1[i]
            outString += word2[i]
        if len(word1) > len(word2):
            outString += word1[shortestStringLen:]
        elif len(word2) > len(word1):
            outString += word2[shortestStringLen:]

        return outString