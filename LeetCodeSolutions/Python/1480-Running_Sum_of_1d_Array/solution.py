class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        outputList = []
        
        for item in nums:
            if len(outputList) == 0:
                outputList.append(item)
            else:
                outputList.append(outputList[-1] + item)
        return outputList