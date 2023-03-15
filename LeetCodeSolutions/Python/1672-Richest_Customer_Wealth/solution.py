# https://leetcode.com/problems/richest-customer-wealth/submissions/915661660/
# Date of Submission: 2023-03-15

# Runtime: 46 ms, faster than 97.77% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 13.8 MB, less than 96.70% of Python3 online submissions for Richest Customer Wealth.
#
# Problem: 
#  You are given an m x n integer grid accounts where accounts[i][j] is the amount 
#  of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
#  A customer's wealth is the amount of money they have in all their bank accounts. 
#  The richest customer is the customer that has the maximum wealth.


#fun ternary operator solution that produces rapid runtime and low memory usage
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0

        for account in accounts:
            maxWealth = sum(account) if sum(account) > maxWealth else maxWealth

        return maxWealth
