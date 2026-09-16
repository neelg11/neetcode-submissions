from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q=collections.deque()
        q.append(root)
        ans=[]
        while(q):
            qlen=len(q)
            temp=[]
            for _ in range(qlen):
                curr=q.popleft()
                if(curr):
                    temp.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if(temp):
                ans.append(temp)

        return ans