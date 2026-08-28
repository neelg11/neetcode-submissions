class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checking box

        for i in range(9):
            visited=[0]*10
            for j in range(9):
                if(board[i][j]=='.'): continue
                num=int(board[i][j])
                if visited[num]: return False
                visited[num]=1
        for j in range(9):
            visited=[0]*10
            for i in range(9):
                if(board[i][j]=='.'): continue
                num=int(board[i][j])
                if visited[num]: return False
                visited[num]=1
        for x in range(0,7,3):
            for y in range(0,7,3):
                visited=[0]*10
                for i in range(3):
                    for j in range(3):
                        if(board[x+i][y+j]=='.'): continue
                        num=int(board[x+i][y+j])
                        if visited[num]: return False
                        visited[num]=1 
        return True
