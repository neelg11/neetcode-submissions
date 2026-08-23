# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth=0
        def check_depth(root):
            if not root: return 0
            return 1+max(check_depth(root.left),check_depth(root.right))
        return check_depth(root)
        