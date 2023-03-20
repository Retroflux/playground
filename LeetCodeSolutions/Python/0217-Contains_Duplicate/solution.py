# https://leetcode.com/problems/contains-duplicate/submissions/918931653/
# Date of Submission: 2023-03-20

# Runtime: 603 ms, faster than 24.59% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 26Mb, less than 99.47% of Python3 online submissions for Contains Duplicate.

#Problem:
#  Given an integer array nums, return true if any value appears at
#  least twice in the array, and return false if every element is distinct. 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        lastNumber = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == lastNumber:
                return True
            lastNumber = nums[i]
        return False