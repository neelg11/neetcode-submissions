class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        up, down = 0, len(matrix)
        ans = []
        while(left<right and up<down):
            #first row:
            for j in range(left,right):
                ans.append(matrix[up][j])
            up+=1
            #right col:
            for i in range(up, down):
                ans.append(matrix[i][right-1])
            right-=1
            if(left==right or up==down):
                break
            #bottom row:
            for j in range(right-1, left-1, -1):
                ans.append(matrix[down-1][j])
            down-=1
            #left col:
            for i in range(down-1, up-1, -1):
                ans.append(matrix[i][left])
            left+=1

        return ans