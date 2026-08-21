class Solution:
    def mySqrt(self, x: int) -> int:
        if(x==0): return 0
        if(x<3): return 1
        left,right=2,x//2
        while(left<=right):
            center=left+(right-left)//2
            sq=center*center
            if(sq==x): return center
            elif(sq>x): right=center-1
            else: left=center+1
        return right