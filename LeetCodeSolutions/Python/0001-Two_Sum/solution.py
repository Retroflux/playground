# https://leetcode.com/problems/two-sum/submissions/920134140/

# Runtime: 62 ms, faster than 76.51% of Python3 online submissions for Two Sum.
# Memory Usage: 15.3 MB, less than 16.46% of Python3 online submissions for Two Sum.

# Problem:
#  Given an array of integers nums and an integer target, return indices 
#  of the two numbers such that they add up to target.
#  You may assume that each input would have exactly one solution,
#  and you may not use the same element twice.
#  You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = dict()
        for i in range(0, len(nums)):
            if hashTable.get(target-nums[i]) != None:
                return [i, hashTable[target-nums[i]]]
            hashTable[nums[i]] = i  # value = index
