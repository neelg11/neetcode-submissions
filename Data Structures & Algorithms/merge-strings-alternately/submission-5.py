class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        l1, l2=len(word1), len(word2)
        i,j=0,0
        while(i<l1 or j<l2):
            if(i<l1 and j<l2):
                res+=word1[i]
                res+=word2[j]
                i+=1
                j+=1
            elif(i>=l1 and j<l2):
                res+=word2[j:]
                j=l2
            elif(i<l1 and j>=l2):
                res+=word1[i:]
                i=l1
        
        return "".join(res)
