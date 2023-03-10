# https://leetcode.com/problems/find-pivot-index/submissions/912853664/
# Date of Submission: 2023-03-10

# Runtime: 149ms, faster than 84.78% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15.2 MB, less than 85.13% of Python3 online submissions for Find Pivot Index.


# Problem:
#Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the
# numbers strictly to the left of the index is equal to the 
# sum of all the numbers strictly to the index's right.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 0
        sumLeft = 0
        sumRight = sum(nums)-nums[0]
        for i in range(1, len(nums)):
            if (sumLeft == sumRight):
                return i-1
            sumLeft += nums[i-1]
            sumRight -= nums[i]
        if sumLeft == sumRight:
            return len(nums)-1
        return -1