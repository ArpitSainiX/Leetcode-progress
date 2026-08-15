// LeetCode Solution: Best Time To Buy And Sell Stock
// Submitted: 2026-08-15T06:02:04.306Z
// Language: Python3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        min_value = float('inf')
        max_value = 0

        for price in prices:
            if price < min_value:
                min_value = price
            profit = price - min_value
            if profit > max_value:
                max_value = profit
        return max_value
        