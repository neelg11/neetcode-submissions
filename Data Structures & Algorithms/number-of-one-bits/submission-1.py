class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        for i in range(32):
            if 1<<i & n: #either something or 000000..
                res+=1
        return res