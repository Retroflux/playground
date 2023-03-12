# https://leetcode.com/problems/largest-perimeter-triangle/submissions/913883655/
# Date of Submission: 2023-03-12

# Runtime: 189ms, faster than 91.20% of Python3 online submissions for Largest Perimeter Triangle.
# Memory Usage: 15.4 MB, less than 36.52% of Python3 online submissions for Largest Perimeter Triangle.

# Problem: Given an integer array nums, return the largest perimeter of 
# a triangle with a non-zero area, formed from three of these lengths. 
# If it is impossible to form any triangle of a non-zero area, return 0.


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()

        for i in range(len(nums)-1, 1, -1):
            if nums[i] < nums[i-1] + nums[i-2]:
                return nums[i] + nums[i-1] + nums[i-2]

        return 0
