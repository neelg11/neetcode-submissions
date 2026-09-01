class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        res=0
        for num in nums:
            if num-1 in numset:
                continue
            len=0
            while(num+len in numset):
                len+=1
            res=max(res,len)
        return res