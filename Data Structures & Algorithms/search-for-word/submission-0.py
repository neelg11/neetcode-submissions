class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board), len(board[0])
        l=len(word)
        visited=[[0]*m for _ in range(n)]

        def dfs(i,j,k):
            if(i<0 or i>=n or j<0 or j>=m or visited[i][j] or board[i][j]!=word[k]):
                return False
            if(board[i][j]==word[k]):
                if(k==l-1):
                    return True
                else:
                    visited[i][j]=1
                    if dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1):
                        return True
                    visited[i][j]=0
                    return False

        for i in range(n):
            for j in range(m):
                if(board[i][j]==word[0]):
                    if dfs(i,j,0):
                        return True
        
        return False
                