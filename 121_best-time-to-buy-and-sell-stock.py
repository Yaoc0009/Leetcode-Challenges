class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, prices[0]
        for i in range(1, len(prices)):
            max_profit = max(prices[i] - min_price, max_profit)
            min_price = min(prices[i], min_price)
        return max_profit
