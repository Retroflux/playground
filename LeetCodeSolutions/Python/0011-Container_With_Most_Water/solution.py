# https://leetcode.com/problems/container-with-most-water/submissions/911561206/
# Date of Submission: 2023-03-08

# Runtime: 712 ms, faster than 90.18% of Python3 online submissions for Container-With-Most_Water.
# Memory Usage: 27.4 MB, less than 45.84% of Python3 online submissions for Container-With-Most_Water.


class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0
        rightPtr = len(height)-1
        windowSize = rightPtr
        leftPtr = 0
        minRec = 0

        while(rightPtr >= leftPtr):

            left = height[leftPtr]
            right = height[rightPtr]
            minRec = min(left,right) * windowSize
            windowSize = rightPtr - leftPtr
            if maxArea < minRec:
                maxArea = minRec
            if left<right:
                leftPtr+=1
            else:
                rightPtr-=1
            windowSize -=1

        return maxArea