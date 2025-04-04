# ID: 121
# Title: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Tags: Array, Dynamic Programming
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for price in prices:
            if price < buy:
                buy = price
            new_profit = price - buy
            if new_profit > profit:
                profit = new_profit
        return profit
