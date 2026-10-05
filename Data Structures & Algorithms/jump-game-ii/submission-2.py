class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        farthest = 0
        steps = 0
        while(farthest<len(nums)-1):
            steps+=1
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])
            l = l+1
            r = farthest
        return steps