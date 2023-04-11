# https://leetcode.com/problems/removing-stars-from-a-string/submissions/931913465/
# Date of Submission: 2022-04-11

# Runtime: 210 ms, faster than 97.58% of Python3 online submissions for Removing Stars From a String.
# Memory Usage: 15.6 MB, less than 40.9% of Python3 online submissions for Removing Stars From a String.

#Problem:
# You are given a string s, which contains stars *.
# In one operation, you can:
#   Choose a star in s.
#   Remove the closest non-star character to its left, as well as remove the star itself.
#   Return the string after all stars have been removed.


class Solution:
    def removeStars(self, s: str) -> str:

        newS = list()
        for char in s:
            if char == "*":
                newS.pop()
            else:
                newS.append(char)
        return ''.join(newS)