# https: // leetcode.com/problems/move-zeroes/submissions/915655326
# Date of Submission: 2023-03-15

# Runtime: 159 ms, faster than 94.70% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15.6 MB, less than 53.8% of Python3 online submissions for Move Zeroes.

# Problem:
#  Given an integer array nums, move all 0's to the end of it while 
#  maintaining the relative order of the non-zero elements.
#  Note that you must do this in -place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        numZeroes = 0
        currIndex = 0

        #move non-zeroes to currIndex (incrementing), count non-zeroes
        for num in nums:
            if num == 0:
                numZeroes += 1
            else:
                nums[currIndex] = num
                currIndex += 1
        
        #overwrite the end of the array with zeroes (numZeroes)
        for i in range(len(nums)-1, len(nums)-1-numZeroes, -1):
            nums[i] = 0
        return
