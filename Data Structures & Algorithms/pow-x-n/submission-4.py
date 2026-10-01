class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = abs(n)
        res=1
        while(power):
            if(power%2): #if unit bit one
                res*=x
            x = x*x
            power = power//2 #power>>1

        if(n>0):
            return res
        return 1/res