# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        prev=TreeNode(0,root,root)
        def post_delete(root,parent,target):
            if(not root): return root
            post_delete(root.left,root,target)
            post_delete(root.right,root,target)
            if(root.val==target and root.left==None and root.right==None):
                    if(parent.left==root):
                        parent.left=None
                    else:
                        parent.right=None
        post_delete(root,prev,target)
        return prev.left
            
