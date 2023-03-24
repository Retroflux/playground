# https://leetcode.com/problems/kth-missing-positive-number/submissions/921489767/
# Date of Submission: 2023-03-24

# Runtime: 63 ms, faster than 24.4% of Python3 online submissions for Kth Missing Positive Integer.
# Memory Usage: 14 MB, less than 74.10% of Python3 online submissions for Kth Missing Positive Integer.
#

# Problem:
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Return the kth positive integer that is missing from this array.


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        currVal = 0
        while k > 0:
            currVal+= 1
            if len(arr) == 0:
                k-=1
            elif currVal < arr[0]:
                k-=1
            elif currVal == arr[0]:
                arr=arr[1:]
        return currVal
