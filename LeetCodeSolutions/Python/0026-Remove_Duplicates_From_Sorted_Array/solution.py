# https://leetcode.com/problems/3sum/submissions/924420848/

# Runtime: 84 ms, faster than 84.8% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.5 MB, less than 94.68% of Python3 online submissions for Remove Duplicates from Sorted Array.

# Problem: Given an integer array nums sorted in non-decreasing order, remove the duplicates 
#  in-place such that each unique element appears only once. The relative order of the 
#  elements should be kept the same. Then return the number of unique elements in nums.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        currPos = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[currPos-1]:
                nums[currPos] = nums[i]
                currPos += 1
        return currPos
