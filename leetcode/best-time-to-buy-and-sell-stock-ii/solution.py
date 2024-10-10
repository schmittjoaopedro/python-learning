from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        totalProfit = 0
        profit = 0

        for price in prices[1:]:
            if price < buyPrice:
                buyPrice = price

            if price - buyPrice >= profit:
                totalProfit -= profit
                profit = price - buyPrice
                totalProfit += profit
            else:
                profit = 0
                buyPrice = price

        return totalProfit
