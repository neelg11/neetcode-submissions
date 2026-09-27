class Solution:
    def reverse(self, x: int) -> int:
        flag=1
        if(x<0):
            flag=-1
            x*=-1
        ans=0
        tens=10
        while(x):
            mod = x % tens
            x = x - mod
            ans = ans * 10
            ans = ans + mod*10//tens
            tens *= 10
        if( ans> 2**31 - 1 or ans < -(2**31)):
            return 0
        return flag*ans
