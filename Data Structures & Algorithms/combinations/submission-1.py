class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        path=[]
        def dfs(i):
            nonlocal ans,path
            if(len(path)==k):
                ans.append(path.copy())
                return
            if(i>n):
                return
            for j in range(i,n+1):
                path.append(j)
                dfs(j+1)
                path.pop()
        dfs(1)
        return ans