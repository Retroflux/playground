# https://leetcode.com/problems/boats-to-save-people/submissions/927275125/
# Date of Submission: 2023-04-03

# Runtime: 1008 ms, faster than 5.5% of Python3 online submissions for Boats to Save People.
# Memory Usage: 19 MB, less than 99.82% of Python3 online submissions for Boats to Save People.

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
        i = len(people) - 1
        numBoats = 0

        if len(people) == 1:
            return 1

        while len(people) > 1:
            if people[i] < limit and people[0] <= limit - people[i]: #remove pair
                people.pop()
                people.pop(0)
                i-=1
            else:
                people.pop()
            i-=1
            numBoats+=1

        return numBoats + len(people)