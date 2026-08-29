class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists=defaultdict(bool)
        for num in nums:
            if exists[num]: return True
            exists[num]=True
        return False