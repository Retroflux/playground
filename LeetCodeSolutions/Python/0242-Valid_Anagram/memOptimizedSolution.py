# https://leetcode.com/problems/valid-anagram/submissions/918921631/
# Date of Submission: 2023-03-20

# Runtime: 195 ms, faster than 5.2% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.4Mb, less than 95.81% of Python3 online submissions for Valid Anagram.

#Problem: 
#  Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#  An Anagram is a word or phrase formed by rearranging the letters of a different word 
#  or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        for char in s:
            if char not in t:
                return False
            t = t.replace(char,"",1)
            s = s.replace(char,"",1)
        if len(s) != 0 or len(t) != 0:
            return False
        return True