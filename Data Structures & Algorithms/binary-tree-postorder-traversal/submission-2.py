# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack,res=[],[]
        last_visited=None
        while(stack or root):
            while(root and (last_visited==None or last_visited!=root.left)):
                stack.append(root)
                root=root.left
            root=stack[-1]
            if(root and root.right and root.right!=last_visited):
                root=root.right
            else:
                res.append(root.val)
                last_visited=stack.pop()
                root=None
        return res
            
                


