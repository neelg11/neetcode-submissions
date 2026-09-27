class Solution:
    def getSum(self, a: int, b: int) -> int:
        bin_a, bin_b = [0]*32, [0]*32
        bin_ans = [0]*32
        for i in range(32):
            bin_a[i] = (a>>i) & 1
            bin_b[i] = (b>>i) & 1
        print(bin_a)
        print(bin_b)
        carry=0
        for i in range(32):
            bin_ans[i] = bin_a[i] ^ bin_b[i] ^ carry
            carry = (bin_a[i] + bin_b[i] + carry)//2
        
        ans=0
        print(bin_ans)
        for i in range(32):
            ans+= (bin_ans[i])*(1<<i)
        if bin_ans[31] == 1:
            ans -= 2**32
        return ans