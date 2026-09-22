class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m=len(grid), len(grid[0])
        ans=0
        def dfs(i,j):
            nonlocal grid
            if(i<0 or i>=n or j<0 or j>=m or grid[i][j]=="0"):
                return
            if(grid[i][j]=="1"):
                grid[i][j]="0"
                if(i+1<n and grid[i+1][j]=='1'):
                    dfs(i+1,j)
                if(i-1>=0 and grid[i-1][j]=='1'):
                    dfs(i-1,j)
                if(j+1<m and grid[i][j+1]=='1'):
                    dfs(i,j+1)
                if(j-1>=0 and grid[i][j-1]=='1'):
                    dfs(i,j-1)
            return
        for i in range(n):
            for j in range(m):
                if(grid[i][j]=="1"):
                    ans+=1
                    dfs(i,j)
        return ans