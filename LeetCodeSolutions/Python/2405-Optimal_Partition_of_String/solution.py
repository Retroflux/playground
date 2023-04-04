# https://leetcode.com/problems/boats-to-save-people/submissions/927275125/
# Date of Submission: 2023-04-04

# Runtime: 86 ms, faster than 96.4% of Python3 online submissions for Optimal Partition of String.
# Memory Usage: 14.6 MB, less than 90.90% of Python3 online submissions for Optimal Partition of String.

# Problem:
#  Given a string s, partition the string into one or more substrings such that the characters in each substring are unique.
#  That is, no letter appears in a single substring more than once.
#  Return the minimum number of substrings in such a partition.
#  Note that each character should belong to exactly one substring in a partition.

 

class Solution:
    def partitionString(self, s: str) -> int:

        numSplits = 1
        currList = ""

        for char in s:
            if char in currList:
                numSplits+=1
                currList = char
            else:
                currList += char
        return numSplits