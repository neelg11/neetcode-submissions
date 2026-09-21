class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        if (total%k!=0): return False
        target=total//k
        for num in nums:
            if(num>target): return False
        bucket=[0]*k
        nums.sort(reverse=True)
        def dfs(i):
            nonlocal bucket
            if(i==len(nums)):
                return all(bucket[b]==target for b in range(k))
            for b in range(k):
                if(bucket[b]+nums[i]>target):
                    continue
                bucket[b]+=nums[i]
                if dfs(i+1):
                    return True
                bucket[b]-=nums[i]
                if(bucket[b]==0):
                    break
            return False
        return dfs(0)
