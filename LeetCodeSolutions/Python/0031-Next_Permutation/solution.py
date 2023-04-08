# https://leetcode.com/problems/next-permutation/submissions/929895676/
# Date of Submission: 2023-04-07

# Runtime: 37 ms, faster than 92.7% of Python3 online submissions for Next Permutation.
# Memory Usage: 15.5 MB, less than 97.72% of Python3 online submissions for Next Permutation.

# Problem:
# Given an array of integers nums, find the next permutation of nums.

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 2

        while i >= 0 and nums[i+1] <= nums[i]:
            i-=1
        
        if i>=0:
            j = len(nums) -1
            while nums[j] <= nums[i]:
                j-=1
            self.swap(nums,i,j)
        self.reverseSubsequence(nums,i+1)
        return
        
    def swap(self, nums, i, j):
        nums[j] += nums[i]
        nums[i] = nums[j] - nums[i]
        nums[j] -= nums[i]   

    def reverseSubsequence(self, nums, i):
        j = len(nums) - 1
        while i<j:
            self.swap(nums,i,j)
            i+=1
            j-=1