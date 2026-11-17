class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        oceans = [[[0,0] for _ in range(m)] for _ in range(n)]
        for i in range(n):
            oceans[i][0][0] = 1 #pacific left
            oceans[i][m-1][1] = 1 #atlantic right
        for j in range(m):
            oceans[0][j][0] = 1 #pacific top
            oceans[n-1][j][1] = 1 #atlantic bottom
        
        directions  = [[0,1], [1,0], [-1,0], [0,-1]]

        q = deque()
        for i in range(n):
            q.append((i,0))
            q.append((i, m-1))
        for j in range(m):
            q.append((0,j))
            q.append((n-1,j))
        
        while q:
            r, c = q.popleft()
            for i, j in directions:
                nr, nc = r+i, c+j
                if nr<0 or nc<0 or nr>=n or nc>=m or heights[r][c]>heights[nr][nc]:
                    continue
                temp = oceans[nr][nc].copy()
                oceans[nr][nc][0]|=oceans[r][c][0]
                oceans[nr][nc][1]|=oceans[r][c][1]
                if temp != oceans[nr][nc]:
                    q.append((nr,nc))

        ans = []
        for i in range(n):
            for j in range(m):
                if oceans[i][j] == [1,1]:
                    ans.append([i,j])
        return ans