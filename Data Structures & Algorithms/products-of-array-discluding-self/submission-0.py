class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix,suffix=[1]*n,[1]*n
        #filling prefix
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        #filling suffix(reverse iteration)
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        #multiply prefix and suffix that's your answer
        ans=[1]*n
        for i in range(n):
            ans[i]=prefix[i]*suffix[i]
        return ans
