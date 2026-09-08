class Solution:
    def simplifyPath(self, path: str) -> str:
        curr=""
        stack=[]
        for c in path+'/':
            if(c=='/'):
                if curr=='..':
                    if(stack):
                        stack.pop()
                elif(curr!="" and curr!='.'):
                    stack.append(curr)
                curr=""
            else:
                curr+=c
        print(stack)
        
        if(not stack):
            return "/"
            
        ans=""
        for s in stack:
            ans+='/'
            ans+=s
        return ans