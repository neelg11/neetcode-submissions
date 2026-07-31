class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()
        if(k<1): return False
        j=0
        for i in range(len(nums)):
            if(i-j>k):
                window.remove(nums[j])
                j+=1
            if(nums[i] in window):
                return True
            window.add(nums[i])
        return False