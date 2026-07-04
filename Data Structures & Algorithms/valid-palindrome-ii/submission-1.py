class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        flag=0
        j=len(s)-1
        while(i<j):
            if(s[i]==s[j]):
                i+=1
                j-=1
            elif flag==0:
                flag=1
                j-=1
            else:
                break
        if(i>=j):
            return True
        i=0
        flag=0
        j=len(s)-1
        while(i<j):
            if(s[i]==s[j]):
                i+=1
                j-=1
            elif flag==0:
                flag=1
                i+=1
            else:
                return False
        return True
        