class Solution:
    def reverseString(self, s: List[str]) -> None:
        i=0
        j=len(s)
        for i in range(0,j//2):
            s[i],s[j-1]=s[j-1],s[i]
            i+=1
            j-=1
        
        