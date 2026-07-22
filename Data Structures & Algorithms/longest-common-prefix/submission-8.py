class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str=""
        for i in zip(*strs):
            if(len(set(i))==1):
                str+=i[0]
            else: return str
        return str
            