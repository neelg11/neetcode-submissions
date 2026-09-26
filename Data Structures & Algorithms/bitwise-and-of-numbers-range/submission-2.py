class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res=0
        for i in range(32):
            if (left>>i) & 1:
                if(right>>i & 1):
                    if right-left<(1<<i):
                        res+=(1<<i)
        return res