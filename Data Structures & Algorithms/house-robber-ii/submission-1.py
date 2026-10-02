class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==1): return nums[0]
        if(n==2): return max(nums[0], nums[1])
        a, b = nums[0], max(nums[0], nums[1])
        i, n = 2, len(nums)
        while(i<n-1):
            temp = b
            b = max ( (nums[i]+a), b )
            a = temp
            i+=1
        ans = max(a,b)
        print(ans)

        a, b = 0, nums[1]
        i, n = 2, len(nums)
        while(i<n):
            temp = b
            b = max ( (nums[i]+a), b )
            a = temp
            i+=1
        return max(a,b,ans)
            
