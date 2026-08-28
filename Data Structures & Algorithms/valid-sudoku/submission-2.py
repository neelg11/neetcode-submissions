class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checking box
        check_rows=[[0]*10 for _ in range(9)]
        check_col=[[0]*10  for _ in range(9)] 
        for x in range(0,7,3):
            for y in range(0,7,3):
                visited=[0]*10
                for i in range(3):
                    for j in range(3):
                        if(board[x+i][y+j]=='.'): continue
                        num=int(board[x+i][y+j])
                        if visited[num]: return False
                        visited[num]=1 

                        if check_rows[x+i][num]: 
                            return False
                        check_rows[x+i][num]=1
                        if check_col[y+j][num]: 
                            return False
                        check_col[y+j][num]=1

        return True
