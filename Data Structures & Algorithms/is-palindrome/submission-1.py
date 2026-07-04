class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=len(s)
        str=""
        for i in range(0,l):
            if(s[i].isalnum()):
                str+=(s[i])
        l=len(str)
        str=str.lower()
        print(str)
        for i in range(0,l//2):
            if(str[i]!=str[l-1-i]):
                return False
        return True
        