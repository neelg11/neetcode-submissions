class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Gagan's: check the part you know is sorted method
        n=len(nums)
        l,r=0,n-1
        while(l<=r):
            m=l+(r-l)//2
            if(nums[m]==target): return True
            if(nums[r]<nums[m]): #left Portion
                if(nums[l]<=target<nums[m]):
                    r=m-1
                else:
                    l=m+1
            elif(nums[m]<nums[r]): # if else both are checking m and l only, 
            #if you check m and r here, issue in this nums=[1,3,1,1,1] target =3
                if(nums[m]<target<=nums[r]): #right Portion
                    l=m+1
                else:
                    r=m-1
            else:
                r-=1
        return False
