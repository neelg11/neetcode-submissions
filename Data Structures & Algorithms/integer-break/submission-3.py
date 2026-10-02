class Solution:
    def integerBreak(self, n: int) -> int:
        if n<4: return n-1
        if n==4: return n
        threes = n//3
        twos = 0
        if(n-3*threes == 1):
            threes-=1
        twos = (n - 3*threes)//2
        return (3**threes)*(2**twos)

            

