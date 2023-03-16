# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/submissions/915649849/
# Date of Submission: 2023-03-15

# Runtime: 64 ms, faster than 58.43% of Python3 online submissions for Sum of All Odd Length Subarrays.
# Memory Usage: 13.7 MB, less than 94.31% of Python3 online submissions for Sum of All Odd Length Subarrays.
#

# Problem:
#  Given an array of positive integers arr, return the sum of all possible 
#  odd-length subarrays of arr. A subarray is a contiguous subsequence of the array.



class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:

        total = sum(arr)

        for i in range(3,len(arr)+1, 2):
            for j in range(0,len(arr)-i+1):
                total +=  sum(arr[j:j+i])
        return total