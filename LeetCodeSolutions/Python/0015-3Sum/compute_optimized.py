# https://leetcode.com/problems/3sum/submissions/924420848/

# Runtime: 889 ms, faster than 97.15% of Python3 online submissions for 3Sum.
# Memory Usage: 19.1 MB, less than 10.15% of Python3 online submissions for 3Sum.

# Problem:
#  Given an integer array nums, return all the triplets [nums[i], nums[j],
#  nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#  Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        outputSet = set()
        zeroCount = 0
        n, p = [], []

        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                zeroCount += 1
        if 0 in nums:
            N, P = set(n), set(p)
            if zeroCount > 0:
                for num in set(P):
                    if -num in N:
                        outputSet.add((-num, 0, num))
            if zeroCount >= 3:
                outputSet.add((0, 0, 0))

        N = set(nums)
        for s in [n, p]:
            for i in range(len(s)):
                for j in range(i + 1, len(s)):
                    target = -(s[i] + s[j])
                    if target in N:
                        outputSet.add(tuple(sorted([s[i], s[j], target])))

        return outputSet
