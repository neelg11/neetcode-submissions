class Solution:
    def climbStairs(self, n: int) -> int:
        if(n<2): return 1
        prev=1
        curr=2
        for i in range(max(n-2,0)):
            tmp=curr+prev
            prev=curr
            curr=tmp
        return curr
