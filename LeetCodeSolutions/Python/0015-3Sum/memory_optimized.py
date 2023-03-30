# https://leetcode.com/problems/3sum/submissions/924420848/

# Runtime: 9940 ms, faster than 5.1% of Python3 online submissions for 3Sum.
# Memory Usage: 18.4 MB, less than 61.17% of Python3 online submissions for 3Sum.

# Problem: 
#  Given an integer array nums, return all the triplets [nums[i], nums[j], 
#  nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#  Notice that the solution set must not contain duplicate triplets.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        outputSet = list()
        leftPointer = 0
        rightPointer = len(nums)-1

        for i in range(0, len(nums)-1):
            checkVal = nums[i] * -1
            leftPointer = i+1
            rightPointer = len(nums)-1
            while leftPointer < rightPointer:
                if nums[leftPointer] + nums[rightPointer] == checkVal:
                    tempList = list()
                    tempList.append(nums[i])
                    tempList.append(nums[leftPointer])
                    tempList.append(nums[rightPointer])
                    if tempList not in outputSet:
                        outputSet.append(tempList)
                    leftPointer += 1
                elif nums[leftPointer] + nums[rightPointer] < checkVal:
                    leftPointer += 1
                else:
                    rightPointer -= 1

        return outputSet
