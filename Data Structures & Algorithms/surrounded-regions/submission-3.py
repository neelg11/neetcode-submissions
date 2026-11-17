class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m  = len(board), len(board[0])
        q = deque()
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        for i in range(n):
            if board[i][0] == "O":
                board[i][0] = "#"
                q.append((i,0))
            if board[i][m-1] == "O":
                board[i][m-1] = "#"
                q.append((i,m-1))
        for j in range(m):
            if board[0][j] == "O":
                board[0][j] = "#"
                q.append((0,j))
            if board[n-1][j] == "O":
                board[n-1][j] = "#"
                q.append((n-1,j))
        
        while q:
            r, c = q.popleft()
            for i, j in directions:
                nr, nc = r+i, c+j
                if nr<0 or nc<0 or nr>=n or nc>=m or board[nr][nc] == "X" or board[nr][nc] == "#":
                    continue
                board[nr][nc] = "#"
                q.append((nr,nc))
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
