class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited=set()
        visited.add('0000')
        for codes in deadends:
            if(codes=='0000'):
                return -1
            visited.add(codes)
        
        def children(parent):
            res=[]
            for i in range(4):
                for move in [-1,1]:
                    digit = str( (int(parent[i])+move)%10 )
                    code = parent[:i] + digit + parent[i+1:]
                    res.append(code)
            return res

        q=deque()
        q.append(['0000',0])
        while(q):
            parent_code, step = q.popleft()
            # if(parent_code == target):
            #     return step
            for child in children(parent_code):
                if(child == target):
                    return step + 1
                if child not in visited:
                    q.append([child,step+1])
                    visited.add(child)
        return -1
