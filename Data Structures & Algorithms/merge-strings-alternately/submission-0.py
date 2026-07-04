class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        a=0
        b=0
        ans=""
        for i in range(0,max(l1,l2)):
            if(a<l1):
                ans+=word1[a]
                a+=1
            if(b<l2):
                ans+=word2[b]
                b+=1
        return ans