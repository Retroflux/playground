# https://leetcode.com/submissions/detail/719094820/
# Date of Submission: 2022-06-10

# Runtime: 59 ms, faster than 92.72% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.8 MB, less than 96.51% of Python3 online submissions for Palindrome Number.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        leftIndex = 0
        rightIndex = len(x)-1
        
        while (leftIndex < rightIndex):
            if (x[leftIndex] != x[rightIndex]):
                return False
            leftIndex+=1
            rightIndex-=1
            
        return True