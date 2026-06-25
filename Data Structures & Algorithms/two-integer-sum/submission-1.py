class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        for i in range(0,l):
            ans=[]
            t=target-nums[i]
            ans.append(i)
            for j in range(0,l):
                if j!=i and nums[j]==t:
                    ans.append(j)
                    return ans