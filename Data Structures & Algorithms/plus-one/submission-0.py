class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        n=len(digits)-1
        for i in range(n,-1,-1):
            if(i==n):
                carry=1
            temp=digits[i]+carry
            print(temp)
            digits[i]=temp%10
            carry=temp//10
        if carry==1:
            digits.insert(0,1)
        return digits


