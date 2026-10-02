class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==1): return nums[0]
        if(n==2): return max(nums[0], nums[1])
        first = nums[0]
        second = max(nums[0], nums[1])
        i=2
        while(i<n):
            temp = second
            second = max ( (nums[i] + first), second )
            first = temp
            i+=1
        return max(first,second)
