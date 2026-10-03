class Solution:
    def climbStairs(self, n: int) -> int:
        from decimal import Decimal, getcontext

        # getcontext().prec = 100
        getcontext().prec = int(n * 0.21) + 10  # number of decimals in fibonccci grows by around 0.21. +10 is safety

        sqrt5 = Decimal(5).sqrt()
        phi = (Decimal(1) + sqrt5) / 2
        
        #psi = 1 - phi
        psi = (Decimal(1) - sqrt5) / 2 
        
        n+=1 
        return round((phi**n - psi**n) / sqrt5)
