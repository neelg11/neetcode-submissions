class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_map={}
        for i in range(len(nums)):
            if(my_map.get(nums[i],-1)==-1):
                my_map[nums[i]]=i
            else:
                if(i-my_map[nums[i]]<=k):
                    return True
                else:
                    my_map[nums[i]]=i
        return False