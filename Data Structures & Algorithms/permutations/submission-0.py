class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used=set()
        ans=[]
        path=[]
        def dfs():
            if(len(path)==len(nums)):
                nonlocal ans
                ans.append(path.copy())
                return

            for i in nums:
                if(i not in used):
                    used.add(i)
                    path.append(i)
                    dfs()
                    path.pop()
                    used.remove(i)
        dfs()
        return ans

