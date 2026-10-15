class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        for i in range(len(prices)):
            if(prices[i] < prices[buy]):
                buy = i
            profit = max(prices[i] - prices[buy], profit)
        return profit