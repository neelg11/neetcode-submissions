class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n,m=len(matrix),len(matrix[0])
        self.mat=matrix
        #doing row sum
        for i in range(n):
            sum=0
            for j in range(m):
                sum+=self.mat[i][j]

            for j in range(0,m):
                tmp=self.mat[i][j]
                self.mat[i][j]=sum
                sum-=tmp
            
        #doing col sum
        for i in range(n-2,-1,-1):
            for j in range(m):
                self.mat[i][j]=self.mat[i][j]+self.mat[i+1][j]
        print(self.mat)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        n=len(self.mat)-1
        m=len(self.mat[0])-1
        full=right=down=diag=0
        full=self.mat[row1][col1]
        if(col2<m):
            right=self.mat[row1][col2+1]
        if(row2<n):
            down=self.mat[row2+1][col1]
        if(row2<n and col2<m):
            diag=self.mat[row2+1][col2+1]
        return full-right-down+diag


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)