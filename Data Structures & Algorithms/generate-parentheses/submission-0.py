class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        curr_open, total_open=1,1
        def dfs(path):
            nonlocal curr_open,total_open
            if(total_open==n):
                temp=path+(')'*curr_open)
                ans.append(temp)
                return
            curr_open+=1
            total_open+=1
            dfs(path+'(')
            curr_open-=1
            total_open-=1

            if(curr_open):
                curr_open-=1
                dfs(path+')')
                curr_open+=1
        dfs('(')
        return ans
