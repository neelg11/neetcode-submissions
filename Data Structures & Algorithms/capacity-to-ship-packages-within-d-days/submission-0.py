class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        while(l<=r):
            mid=l+(r-l)//2
            curr_weight=0
            curr_days=0
            for i,num in enumerate(weights):
                if(curr_weight+num<=mid):
                    curr_weight+=num
                else:
                    curr_weight=num
                    curr_days+=1
                if(i==len(weights)-1):
                    curr_days+=1
            if(curr_days<=days):
                r=mid-1
                res=mid
            else:
                l=mid+1
        return res
               