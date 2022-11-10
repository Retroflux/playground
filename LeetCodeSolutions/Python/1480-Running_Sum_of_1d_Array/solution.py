# https://leetcode.com/submissions/detail/718302600/
# Date of Submission: 2022-06-09

# Runtime: 85 ms, faster than 98.93% of Python online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14.3 MB, less than 24.75% of Python3 online submissions for Median of Two Sorted Arrays.


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        outputList = []
        
        for item in nums:
            if len(outputList) == 0:
                outputList.append(item)
            else:
                outputList.append(outputList[-1] + item)
        return outputList