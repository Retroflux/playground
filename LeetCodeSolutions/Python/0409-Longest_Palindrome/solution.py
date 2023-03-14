# https://leetcode.com/problems/longest-palindrome/submissions/915010587
# Date of Submission: 2023-03-14

# Runtime: 35 ms, faster than 60.39% of Python3 online submissions for Longest Palindrome.
# Memory Usage: 13.8 MB, less than 95.88% of Python3 online submissions for Longest Palindrome.
#

# Problem:
#  Given a string s which consists of lowercase or uppercase letters, return the length of the 
#  longest palindrome that can be built with those letters.
#  Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution:
    def longestPalindrome(self, s: str) -> int:

        maxOdd = 1
        currCharCount = 0
        s = sorted(s)
        previousChar = s[0]

        for char in s:
            if previousChar == char:
                currCharCount+=1
                continue
            else:
                if currCharCount % 2 == 1:
                    maxOdd -= 1
                currCharCount = 1
                previousChar = char
        if currCharCount % 2 == 1:
            maxOdd -= 1
        
        if maxOdd == 1:
            return len(s)
        else:
            return len(s) + maxOdd 