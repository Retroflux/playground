# https://leetcode.com/problems/3sum/submissions/924420848/

# Runtime: 31 ms, faster than 84.42% of Python3 online submissions for Remove Element.
# Memory Usage: 13.7 MB, less than 95.18 of Python3 online submissions for Remove Element.

# Problem: 

# Given an integer array nums and an integer val, remove all occurrences of val 
# in nums in -place. The order of the elements may be changed. Then return the 
# number of elements in nums which are not equal to val.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
