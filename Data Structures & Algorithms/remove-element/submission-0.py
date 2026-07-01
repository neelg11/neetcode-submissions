class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        for i in nums:
            if i==val:
                count+=1
        ans=len(nums)-count
        while count:
            nums.remove(val)
            count-=1
        return ans
        