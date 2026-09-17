class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        buy = 0
        sell = 0

        while buy < len(prices) and sell < len(prices):
            profit = prices[sell] - prices[buy]
            
            if profit >= 0:
                best_profit = max(best_profit, profit)
                sell += 1
            else:
                buy += 1

        return best_profit