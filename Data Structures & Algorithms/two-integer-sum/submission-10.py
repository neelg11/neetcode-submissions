class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited=defaultdict(int)
        for i,num in enumerate(nums):
            remaining=target-num
            if remaining in visited.keys():
                return [visited[remaining],i]
            visited[num]=i