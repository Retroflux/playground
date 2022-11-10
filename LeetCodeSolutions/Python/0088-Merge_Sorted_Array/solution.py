# https://leetcode.com/submissions/detail/743908556/
# Date of Submission: 2022-07-11

# Runtime: 43 ms, faster than 83.57% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.9 MB, less than 85.55% of Python3 online submissions for Merge Sorted Array.



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m+ n == 0:  # no data case
            return
        elif len(nums1) == m:  # nums1 has all the values
            return
        elif len(nums2) == m + n:  # nums2 has all the values
            for i in range(0, len(nums2)):
                nums1[i] = nums2[i]
            return

        position = m + n - 1  # last position in nums1
        m -= 1
        n -= 1

        # empty out the list with the largest minimum number
        while (m > -1 and n > -1):
            if (nums2[n] >= nums1[m]):
                nums1[position] = nums2[n]

                n -= 1
            else:
                nums1[position] = nums1[m]
                m -= 1

            position -= 1

        # empty whichever list still has numbers into the remaining array fields
        while (m >= 0):
            nums1[position] = nums1[m]
            m -= 1
            position -= 1
        # empty list2 if anything remains
        while (n >= 0):
            nums1[position] = nums2[n]
            n -= 1
            position -= 1
        return
