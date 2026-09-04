class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        ln=len(nums)
        res=[]
        for i in range(ln):
            if(i and nums[i]==nums[i-1]):
                continue
            for j in range(i+1,ln):
                if(j>i+1 and nums[j]==nums[j-1]):
                    continue
                curr_target=target-nums[i]-nums[j]
                print(f"i:{nums[i]}, j:{nums[j]}, ct:{curr_target}")
                l,r=j+1,ln-1
                while(l<r):
                    if(nums[l]+nums[r]==curr_target):
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while(l<r and nums[l]==nums[l-1]): l+=1
                        while(l<r and nums[r]==nums[r+1]): r-=1
                    elif(nums[l]+nums[r]>curr_target):
                        r-=1
                    else:
                        l+=1
        return res