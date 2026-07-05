class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        ans=0
        if(l==1):
            return ans
        for i in range(l):
            for j in range(i+1,l):
                ans=max(prices[j]-prices[i],ans)
        return ans