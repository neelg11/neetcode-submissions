import numpy as np
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        a=np.array(arr)
        a=abs(a-x)
        l,r=0,len(arr)-1
        while r-l>=k:
            if(a[l]<=a[r]):
                r-=1
            else:
                l+=1
        return arr[l:r+1]