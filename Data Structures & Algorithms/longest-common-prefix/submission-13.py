class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=min(strs,key=len)
        l=len(l)
        ans=""
        for j in range(l):
            for i in range(1,len(strs)):
                if(strs[i][j]!=strs[i-1][j]):
                    return ans
            ans+=strs[0][j]
        return ans

           
