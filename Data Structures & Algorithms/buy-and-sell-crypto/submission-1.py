class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,buy=0,0
        for i in range(len(prices)):
            profit=max(profit,prices[i]-prices[buy])
            if(prices[i]-prices[buy])<0:
                buy=i
        return profit