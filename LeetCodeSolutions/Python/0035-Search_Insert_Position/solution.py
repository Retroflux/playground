# https://leetcode.com/problems/search-insert-position/submissions/931446007/
# Date of Submission: 2022-07-07
# Updated: 2023-04-10

# Runtime: 39 ms, faster than 99.19% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.6 MB, less than 71.15% of Python3 online submissions for Search Insert Position.

#Problem:


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target <= nums[0]:
            return 0

        insertPoint = 0
        
        while len(nums) > 1 :
            
            splitPoint = int(len(nums)/2)
            
            if target >= nums[splitPoint]:
                nums = nums[splitPoint:]
                insertPoint = insertPoint + splitPoint
            else:
                nums = nums[:splitPoint]
            
            if nums[0] == target:
                return insertPoint

        return insertPoint + 1