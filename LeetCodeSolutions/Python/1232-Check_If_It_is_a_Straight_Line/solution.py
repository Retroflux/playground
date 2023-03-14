# https://leetcode.com/problems/check-if-it-is-a-straight-line/submissions/915083954/
# Date of Submission: 2023-03-14

# Runtime: 60 ms, faster than 82.61% of Python3 online submissions for Check If It Is a Straight Line.
# Memory Usage: 14.3 MB, less than 70.50% of Python3 online submissions for Check If It Is a Straight Line.

# Problem:
#  You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
#  Check if these points make a straight line in the XY plane.

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        rise = coordinates[1][1] - coordinates[0][1]
        run = coordinates[1][0] - coordinates[0][0]

        for i in range(1,len(coordinates)):
            curr_rise=coordinates[i][1]-coordinates[i-1][1]
            curr_run=coordinates[i][0]-coordinates[i-1][0]
            
            if(rise*curr_run != run*curr_rise):
                return False;  
            
        return True