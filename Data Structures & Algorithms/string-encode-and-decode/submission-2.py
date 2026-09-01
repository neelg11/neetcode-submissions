class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res=[]
        i,n=0,len(s)
        while(i<n):
            j=i
            while(s[j]!='#'):
                j+=1
            length=int(s[i:j])
            i=j+1
            start=i
            end=i+length
            res.append(s[start:end])
            i=end
        return res

