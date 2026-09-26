class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        bin_a, bin_b = [0]*32, [0]*32
        bin_ans = [0]*32
        for i in range(32):
            bin_a[i] = (a>>i) & 1
            bin_b[i] = (b>>i) & 1
        
        carry=0
        for i in range(32):
            bin_ans[i] = bin_a[i] ^ bin_b[i] ^ carry
            carry = (bin_a[i] + bin_b[i] + carry)//2
        
        ans=0
        for i in range(32):
            ans+= (bin_ans[i])*(1<<i)
        if ans > 0x7FFFFFFF:
            ans = ~(ans ^ mask)
        return ans