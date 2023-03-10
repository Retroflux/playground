# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/submissions/912802401/
# Date of Submission: 2023-03-10

# Runtime: 24 ms, faster than 97.45% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
# Memory Usage: 13.7 MB, less than 93.10% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
#

# Problem:
# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
from math import mean

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        return mean(salary)
