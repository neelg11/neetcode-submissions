class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        ans=[]
        if not digits:
            return ans
        
        charmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        path=[]
        def dfs(i):
            nonlocal ans,path
            if(i>=len(digits)):
                ans.append("".join(path))
                return
            for c in charmap[digits[i]]:
                path.append(c)
                dfs(i+1)
                path.pop()
        dfs(0)
        return ans
                
