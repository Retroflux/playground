# https://leetcode.com/problems/boats-to-save-people/submissions/927275125/
# Date of Submission: 2023-04-03

# Runtime: 451 ms, faster than 87.81% of Python3 online submissions for Boats to Save People.
# Memory Usage: 20.9 MB, less than 60.46% of Python3 online submissions for Boats to Save People.

# Problem:
#  You are given an array people where people[i] is the weight of the ith person, and an 
#  infinite number of boats where each boat can carry a maximum weight of limit. Each 
#  boat carries at most two people at the same time, provided the sum of the weight 
#  of those people is at most limit.
# 
#  Return the minimum number of boats to carry every given person.


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        rightPtr = len(people) - 1
        leftPtr = 0
        numBoats = 0

        if len(people) == 1:
            return 1

        while leftPtr < rightPtr:
            if people[rightPtr] < limit and people[leftPtr] <= limit - people[rightPtr]: #remove pair
                rightPtr-=1
                leftPtr+=1
            else:
                rightPtr-=1
            numBoats+=1
        if leftPtr == rightPtr:
            return numBoats + 1
        return numBoats