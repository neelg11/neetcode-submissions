class Solution:
    def sortColors(self, nums: List[int]) -> None:
        one=two=zero=0
        for two in range(len(nums)):
            tmp=nums[two]
            nums[two]=2
            two+=1
            if(tmp<2):
                nums[one]=1
                one+=1
            if(tmp<1):
                nums[zero]=0
                zero+=1
        