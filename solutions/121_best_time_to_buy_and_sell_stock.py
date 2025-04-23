# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List
import unittest

# This solution finds the maximum profit from stock prices using a sliding window approach. 
# Time: O(n), Space: O(1). Efficiently tracks the lowest price and maximum profit in one pass.

def maxProfit(prices: List[int]) -> int:
    profit = 0
    left = 0
    right = 1
    while right < len(prices):
        currentProfit = prices[right] - prices[left]
        if prices[left] < prices[right]:
            profit = max(profit, currentProfit)
        else:
            left = right
        right += 1
    return profit

class TestMyFunctions(unittest.TestCase):
    def test_maxProfit1(self):
        self.assertEqual(maxProfit([7,1,5,3,6,4]), 5)
    def test_maxProfit2(self):
        self.assertEqual(maxProfit([7,6,4,3,1]), 0)
if __name__ == '__main__':
    unittest.main()