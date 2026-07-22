class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        list=[]
        for i in zip(*strs):
            if(len(set(i))==1):
                list.append(i[0])
            else: break
        a="".join(list)
        return a
            