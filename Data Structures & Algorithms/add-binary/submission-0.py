class Solution:
    def addBinary(self, a: str, b: str) -> str:
        char_to_int={'0':0, '1':1}
        carry=0
        a=a[::-1]
        b=b[::-1]
        res=""
        for i in range(max(len(a),len(b))):
            num_a,num_b=0,0
            if(i<len(a)):
                num_a=char_to_int[a[i]]
            if(i<len(b)):
                num_b=char_to_int[b[i]]
           
            addition=num_a+num_b+carry
            char=str(addition%2)
            res=char+res
            carry=addition//2
            
        if(carry):
            res='1'+res
        return res
                