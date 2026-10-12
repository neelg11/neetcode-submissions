class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element, count = 0, 0
        for num in nums:
            if count == 0:
                element = num
                count += 1
            elif num == element:
                count += 1
            else:
                count -= 1
        return element