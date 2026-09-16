# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(not root): return []
        q=collections.deque()
        q.append(root)
        res=[]
        while(q):
            qlen=len(q)
            curr_ans=None
            for i in range(qlen):
                curr=q.popleft()
                if curr:
                    curr_ans=curr
                    q.append(curr.left)
                    q.append(curr.right)
            if curr_ans:
                res.append(curr_ans.val)
        return res
