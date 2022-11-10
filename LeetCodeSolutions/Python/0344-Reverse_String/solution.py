# https://leetcode.com/submissions/detail/719220174/
# Date of Submission: 2022-06-10

# Runtime: 211 ms, faster than 81.37% of Python3 online submissions for Reverse String.
# Memory Usage: 18.4 MB, less than 87.15% of Python3 online submissions for Reverse String.


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp = ""
        for i in range(0,int(len(s)/2)):
            temp = s[i]
            s[i] = s[-(i+1)]
            s[-(i+1)] = temp            
