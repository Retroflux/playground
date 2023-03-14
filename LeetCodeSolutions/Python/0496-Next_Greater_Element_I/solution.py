# https://leetcode.com/problems/middle-of-the-linked-list/submissions/914581005/
# Date of Submission: 2023-03-14

# Runtime: 149 ms, faster than 14.38% of Python3 online submissions for Next Greater Element I.
# Memory Usage: 14.1 MB, less than 92.74% of Python3 online submissions for Next Greater Element I.

# Problem:
#  The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
#  You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
#  For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
#  If there is no next greater element, then the answer for this query is -1.
#  Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        outputList = list()

        for num in nums1:
            if num == max(nums2[nums2.index(num):]):
                outputList.append(-1)
                continue
            for j in range(nums2.index(num),len(nums2)):
                if nums2[j] > num:
                    outputList.append(nums2[j])
                    break
        return outputList