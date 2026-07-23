class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        remaining={}
        for i in range(len(nums)):
            left=target-nums[i]
            if(left in remaining):
                return [remaining[left],i]
            remaining[nums[i]]=i