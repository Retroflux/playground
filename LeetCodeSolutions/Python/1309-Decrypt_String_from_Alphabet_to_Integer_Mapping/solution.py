# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/submissions/917646652/
# Runtime: 28 ms, faster than 88.91% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
# Memory Usage: 13.9 MB, less than 54.70% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
#
# Problem:
#  You are given a string s formed by digits and '#'. We want to map s to English 
#  lowercase characters as follows:
#     Characters('a' to 'i') are represented by('1' to '9') respectively.
#     Characters('j' to 'z') are represented by('10#' to '26#') respectively.
#     Return the string formed after mapping.
# The test cases are generated so that a unique mapping will always exist.

class Solution:
    def freqAlphabets(self, s: str) -> str:

        letterGroups = s.split("#")
        if s[-1] != '#':
            letterGroups = letterGroups[:-1] + list(letterGroups[-1])

        revisedString = ""

        for letterGroup in letterGroups:
            if len(letterGroup) == 0:
                continue
            while len(letterGroup) > 2:
                revisedString += (chr(int(letterGroup[0]) + 96))
                letterGroup = letterGroup[1:]

            revisedString += (chr(int(letterGroup) + 96))

        return revisedString
