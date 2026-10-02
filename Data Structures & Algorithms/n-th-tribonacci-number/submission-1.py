class Solution:
    def tribonacci(self, n: int) -> int:
        if(n<2):
            return n
        if(n==2):
            return 1
        a, b, c = 0, 1, 1
        while(n>=3):
            temp = c
            c = a + b + c

            temp2 = b
            b = temp

            a = temp2
            n-=1
        return c