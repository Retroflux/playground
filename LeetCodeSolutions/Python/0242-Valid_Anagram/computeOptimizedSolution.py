# https://leetcode.com/problems/valid-anagram/submissions/918923159/
# Date of Submission: 2023-03-20

# Runtime: 50 ms, faster than 68.21% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15.2Mb, less than 10.55% of Python3 online submissions for Valid Anagram.

#Problem: 
#  Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#  An Anagram is a word or phrase formed by rearranging the letters of a different word 
#  or phrase, typically using all the original letters exactly once.

class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
      return sorted(s) == sorted(t)