class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        j=0
        ans=[]
        while i<m and j<n:
            if(nums1[i]>=nums2[j]):
                ans.append(nums2[j])
                j+=1
            else:
                ans.append(nums1[i])
                i+=1
        if i==m:
            while j<n:
                ans.append(nums2[j])
                j+=1
        else:
            while i<m:
                ans.append(nums1[i])
                i+=1
        for i in range(0,m+n):
            nums1[i]=ans[i]