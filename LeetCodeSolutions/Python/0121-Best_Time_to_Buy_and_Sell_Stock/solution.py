# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/915059305/
# Date of Submission: 2023-03-14

# Runtime: 936 ms, faster than 94.22% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 13.8 MB, less than 97.14% of Python3 online submissions for Best Time to Buy and Sell Stock.
#

# Problem:
#  You are given an array prices where prices[i] is the price of a given stock on the ith day.
#  You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#  Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#Greedy algorithm solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestPrice = 0
        buyPrice = prices[0]
        
        for price in prices:
            if price < buyPrice:
                buyPrice = price
                continue
            if price - buyPrice > bestPrice:
                bestPrice = price - buyPrice
        return bestPrice