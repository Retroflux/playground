
# https://leetcode.com/submissions/detail/718171829/
# Date of Submission: 2022-06-09

# Runtime: 85 ms, faster than 98.93% of Python online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14.3 MB, less than 24.75% of Python3 online submissions for Median of Two Sorted Arrays.

#TODO Refactor this code to remove the duplication throughout, if possible. Happy with runtime, but sloppy.


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        
        
        totalLength = len(nums1) + len(nums2)
        isEven = 1 if(totalLength % 2 == 0) else 0
        
        nums1Position = 0
        nums2Position = 0
        stopCounter = ceil(totalLength/2)
        retVal = 0.0
        
        if(len(nums1) == 0):
            if(len(nums2) == 1):
                return nums2[0]
            nums2Position = ceil(len(nums2)/2)-1
            nums1Position = 1001
        elif(len(nums2) == 0):
            if(len(nums1) == 1):
                return nums1[0]
            nums1Position = ceil(len(nums1)/2)-1
            nums2Position = 1001
        else:
            while(stopCounter > 1):
                if (nums1Position >= len(nums1)):
                    nums2Position+=1
                elif (nums2Position >= len(nums2)):
                    nums1Position+=1
                elif (nums1[nums1Position] < nums2[nums2Position]):
                    nums1Position+=1
                else:
                    nums2Position+=1
                stopCounter-=1
        #Odd/Even Base Case
        if(nums1Position >= len(nums1)):
            retVal = nums2[nums2Position]
            nums2Position+=1
        elif(nums2Position >= len(nums2)):
            retVal = nums1[nums1Position]
            nums1Position+=1

        elif nums1[nums1Position] < nums2[nums2Position]:
            retVal = nums1[nums1Position]
            nums1Position+=1
        else:
            retVal = nums2[nums2Position]
            nums2Position+=1
        # retVal = nums1[nums1Position] if nums1[nums1Position] < nums2[nums2Position] else nums2[nums2Position]
            
    
        #Even Case Augmentation
        if (isEven):
            if (nums1Position >= len(nums1))  :
                retVal = (retVal + nums2[nums2Position])/2
            elif (nums2Position >= len(nums2)):
                retVal = (retVal + nums1[nums1Position])/2
            elif (nums2Position >= len(nums2) or nums1[nums1Position] < nums2[nums2Position]):
                retVal = (retVal + nums1[nums1Position])/2
            else:
                retVal = (retVal + nums2[nums2Position])/2
        
        return retVal