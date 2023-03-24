# https://leetcode.com/problems/kth-missing-positive-number/submissions/921489767/
# Date of Submission: 2023-03-24

# Runtime: 40 ms, faster than 99.3% of Python3 online submissions for Kth Missing Positive Integer.
# Memory Usage: 13.9 MB, less than 74.10% of Python3 online submissions for Kth Missing Positive Integer.
#

# Problem:
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Return the kth positive integer that is missing from this array.

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        arr.insert(0, 0)

        for i in range(0, len(arr)-1):
            difference = arr[i+1] - arr[i]-1
            if k <= (difference):  # if k == 2 and 8-5-1 = 2
                return arr[i] + k
            else:
                k -= difference
        return arr[len(arr)-1]+k
