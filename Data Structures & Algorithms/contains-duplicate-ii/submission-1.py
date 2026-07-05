class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=len(nums)
        for i in range(0,l):
            if(nums[i] in nums[i+1:i+1+k]):
                return True
        return False