# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack=[root]
        depth_stack=[1]
        res=0
        while(stack):
            curr=stack.pop()
            depth=depth_stack.pop()
            if(curr):
                res=max(res, depth)
                stack.append(curr.left)
                depth_stack.append(depth+1)
                stack.append(curr.right)
                depth_stack.append(depth+1)
        return res