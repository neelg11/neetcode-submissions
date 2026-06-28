class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ll=len(strs)
        l=300
        i=0
        while i<ll:
            if(len(strs[i])<l):
                l=len(strs[i])
            i+=1
        i=0
        ans=""
        while i<l:
            for j in range(0,ll-1):
                if(strs[j][i]!=strs[j+1][i]):
                    return ans
            ans+=strs[0][i]
            i+=1
        return ans