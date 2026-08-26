class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m=len(matrix),len(matrix[0])
        up,down=0,n-1
        row=-1
        while(up<=down):
            mid=up+(down-up)//2
            if(target==matrix[mid][0]): return True
            if(target>matrix[mid][0]):
                row=mid
                up=mid+1
            else:
                down=mid-1
        print(row)
        left,right=0,m-1
        while(left<=right):
            col=left+(right-left)//2
            if(target==matrix[row][col]): return True
            elif(target>matrix[row][col]): left=col+1
            else: right=col-1
        return False