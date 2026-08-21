class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        add_pos=m+n-1
        p1=m-1
        p2=n-1
        while(add_pos>=0):
            if(p1>=0 and p2>=0):
                if(nums1[p1]<nums2[p2]):
                    nums1[add_pos]=nums2[p2]
                    p2-=1
                    add_pos-=1
                elif(nums1[p1]>=nums2[p2]):
                    nums1[add_pos]=nums1[p1]
                    p1-=1
                    add_pos-=1
            else:
                while(p1>=0):
                    nums1[add_pos]=nums1[p1]
                    p1-=1
                    add_pos-=1
                while(p2>=0):
                    nums1[add_pos]=nums2[p2]
                    p2-=1
                    add_pos-=1
                

        