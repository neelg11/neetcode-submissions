class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        dir = [[0,1], [1,0], [-1,0], [0,-1]]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
        while q:
            r, c = q.popleft()
            for i, j in dir:
                nr, nc = r+i, c+j
                if (nr<0 or nc<0 or nr>=n or nc>=m or grid[nr][nc]<=grid[r][c]+1):
                    continue
                grid[nr][nc] = grid[r][c]+1
                q.append((nr,nc))