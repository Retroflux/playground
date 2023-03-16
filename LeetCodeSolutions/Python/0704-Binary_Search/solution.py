# https://leetcode.com/problems/binary-search/submissions/916329369/
# Date of Submission: 2023-03-16

# Runtime: 233 ms, faster than 95.31% of Python3 online submissions for Binary Search.
# Memory Usage: 15.4 MB, less than 96.85% of Python3 online submissions for Binary Search.

# Problem:
# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. If target exists, 
# then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        binarySearchResult = binSearch(nums, target, 0)
        return binarySearchResult


def binSearch(subset, target, leftIndex):
    # exit case
    if len(subset) == 1:
        if subset[0] == target:
            return leftIndex
        else:
            return -1
    else:
        left = subset[:int(len(subset)/2)]
        right = subset[int(len(subset)/2):]

        # short circuit, left-edge checks before recursing
        if left[len(left)-1] >= target:
            if left[len(left)-1] == target:
                return leftIndex + len(left)-1
            else:
                return binSearch(left, target, leftIndex)
        else:
            if right[0] == target:
                return leftIndex + int(len(subset)/2)
            else:
                return binSearch(right, target, leftIndex + int(len(subset)/2))