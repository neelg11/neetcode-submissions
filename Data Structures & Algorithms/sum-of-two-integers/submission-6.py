class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1<<12)-1
        max_int = (1<<11) - 1
        
        while(b):
            carry = (a&b) << 1
            a = (a^b) & mask
            b = carry & mask
        if(a>max_int):
            return a - (1<<12)
        return a
