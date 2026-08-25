class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        profit=0
        curr_profit=0
        for i in range(1,len(prices)):
            if(prices[i]-prices[buy]<curr_profit):
                buy=i
                profit+=curr_profit
                curr_profit=0
            else:
                curr_profit=prices[i]-prices[buy]
        print(curr_profit)
        return profit+curr_profit