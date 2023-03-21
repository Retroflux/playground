# https://leetcode.com/problems/range-sum-query-immutable/submissions/919804167

# Runtime: 1110 ms, faster than 25.87% of Python3 online submissions for Range Sum Query Immutable.
# Memory Usage: 17.4 MB, less than 98.3% of Python3 online submissions for Range Sum Query Immutable.

# Problem:
#  Given an integer array nums, handle multiple queries of the following type:
#  Calculate the sum of the elements of nums between indices left and right 
# inclusive where left <= right.

# Implement the NumArray class:
#     NumArray(int[] nums) Initializes the object with the integer array nums.
#     int sumRange(int left, int right) Returns the sum of the elements of nums 
#     between indices left and right inclusive(i.e. nums[left] + nums[left + 1] + ... + 
#     nums[right]).



class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
