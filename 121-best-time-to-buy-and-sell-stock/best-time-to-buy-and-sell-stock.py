class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit=0
        n=len(prices)
        a=prices[0]
        for i in range(1,n):
            profit = prices[i] - a
            if max_profit < profit:
                max_profit = profit
            if prices[i] < a:
                a = prices[i]
        return max_profit