class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        subset=[]
        def dfs(i):
            nonlocal ans
            if(len(subset)==k):
                ans.append(subset.copy())
                return
            if(i>n): return 
            dfs(i+1)

            subset.append(i)
            dfs(i+1)
            subset.pop()
            
        dfs(1)
        return ans