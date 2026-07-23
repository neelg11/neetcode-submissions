class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        for i in zip(*strs):
            temp=i[0]
            for j in i:
                if(j!=temp): return ans
                temp=j
            ans+=temp
        return ans