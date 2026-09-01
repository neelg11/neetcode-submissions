class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        ans=0
        for i in nums:
            if (i-1) in numset:
                continue
            count=0
            while(i+count in numset):
                count+=1
            ans=max(ans,count)
        return ans

