class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n, m = len(grid), len(grid[0])
        ans=0
        count=0
        q=deque()
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==2):
                    q.append([i,j,0])
                if(grid[i][j]==1):
                    count+=1
        while(q):
            row, col, time = q.popleft()
            ans=max(time,ans)
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if(nr<0 or nc<0 or nr>=n or nc>=m or grid[nr][nc]%2==0):
                    continue
                grid[nr][nc]=2
                count-=1
                q.append([nr,nc,time+1])
        if(count): return -1
        return ans