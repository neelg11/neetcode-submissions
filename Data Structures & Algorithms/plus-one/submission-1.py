class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits)-1
        while (carry and i>=0):
            digit = digits[i]
            digits[i] = (digit+carry)%10 
            carry = (digit + carry) // 10
            i-=1
        if(carry == 1):
            digits.insert(0, 1)
        return digits
            