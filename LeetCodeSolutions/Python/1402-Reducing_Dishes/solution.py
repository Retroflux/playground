# https://leetcode.com/problems/reducing-dishes/submissions/924221929/
# Date of Submission: 2023-03-29

# Runtime: 37 ms, faster than 91.14% of Python3 online submissions for Reducing Dishes.
# Memory Usage: 13.8 MB, less than 98.73% of Python3 online submissions for Reducing Dishes.
#

# Problem:
#  A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
#   
#  Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].
#  Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.
#   
#  Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()
        
        totalSatisfaction = 0
        maxTotalSatisfaction = 0
        numDishes = len(satisfaction)

        for i in range(numDishes-1,-1,-1): 
            if satisfaction[i] <= totalSatisfaction*-1:
                break
            totalSatisfaction += satisfaction[i]
            maxTotalSatisfaction += totalSatisfaction
        return maxTotalSatisfaction
