class Solution:
    def mySqrt(self, x: int) -> int:
        left, right=0, x
        mid=-1
        while(left<=right):
            mid=left+(right-left)//2
            check=mid**2
            if(check==x):
                return mid
            elif(check>x):
                right=mid-1
            else:
                left=mid+1
        if mid**2>x:
            mid-=1
        return mid