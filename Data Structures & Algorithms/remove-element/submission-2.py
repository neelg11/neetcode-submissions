class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        tmp = []
        for num in nums:
            if num == val:
                continue
            tmp.append(num)
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)
    
    # def removeElement(self, nums: List[int], val: int) -> int:
        # count=0
        # l=len(nums)
        # for i in nums:
        #     if i==val:
        #         count+=1
        # ans=len(nums)-count
        # j=l-1
        # for i in range(0,ans):
        #     while nums[j]== val:
        #         j-=1
        #     if nums[i]==val:
        #         nums[i], nums[j]=nums[j], nums[i]
        #         j-=1
        # return ans
        
        