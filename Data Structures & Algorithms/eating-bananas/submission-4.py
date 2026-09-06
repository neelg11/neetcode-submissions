import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        ans=r
        while(l<=r):
            count=0
            mid=l+(r-l)//2
            for i in piles:
                count+=math.ceil(float(i)/mid)
            if count<=h:
                ans=min(ans,mid)
                r=mid-1
            else:
                l=mid+1
        return ans