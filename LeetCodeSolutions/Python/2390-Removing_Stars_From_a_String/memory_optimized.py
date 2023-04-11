# https://leetcode.com/problems/removing-stars-from-a-string/submissions/931906591/
# Date of Submission: 2022-04-11

# Runtime: 4205 ms, faster than 5.7% of Python3 online submissions for Removing Stars From a String.
# Memory Usage: 15 MB, less than 99.88% of Python3 online submissions for Removing Stars From a String.

#Problem:
# You are given a string s, which contains stars *.
# In one operation, you can:
#   Choose a star in s.
#   Remove the closest non-star character to its left, as well as remove the star itself.
#   Return the string after all stars have been removed.


class Solution:
    def removeStars(self, s: str) -> str:
        stars = s.count("*")

        while stars > 0:

            location = s.find("*")

            s = s[:location-1] + s[location+1:]
            stars -= 1
        return s