from collections import defaultdict
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        freq_map=defaultdict(int)
        for num in nums:
            freq_map[num]+=1
        path=[]
        ans=[]
        def dfs():
            if(len(path)==len(nums)):
                ans.append(path.copy())
                return
            for num in freq_map.keys():
                if(freq_map[num]):
                    freq_map[num]-=1
                    path.append(num)

                    dfs()

                    freq_map[num]+=1
                    path.pop()
        dfs()
        return ans