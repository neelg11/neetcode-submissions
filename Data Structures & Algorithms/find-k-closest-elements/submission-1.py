class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff,idx=100000,-1
        n=len(arr)
        for i,num in enumerate(arr):
            if(abs(num-x)<diff):
                diff=abs(num-x)
                idx=i
        res=[arr[idx]]
        left=idx-1
        right=idx+1
        while(len(res)<k):
            if(left>=0 and right<n):
                if(abs(arr[left]-x)<=abs(arr[right]-x)):
                    res.append(arr[left])
                    left-=1
                else:
                    res.append(arr[right])
                    right+=1
            elif(left>=0):
                res.append(arr[left])
                left-=1
            elif(right<n):
                res.append(arr[right])
                right+=1
        return sorted(res)
