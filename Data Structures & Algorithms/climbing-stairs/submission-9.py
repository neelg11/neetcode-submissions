class Solution:
    def climbStairs(self, n: int) -> int:
        if n<4: 
            return n
        #dp[i] = dp [i-1] + dp [i-2] ## jump of 1 from i-1, and jump of 2 from i-2, jump of 1+1 from 
        #i-2 is included in, i-2 + 2
        a, b = 2, 3 
        for i in range(n-3):
            temp = b
            b = a+b
            a = temp
        return b
        
