# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root: return root
        #search and call 
        prev=TreeNode(0,root,root)
        ans=prev
        while(root and root.val!=key):
            prev=root
            if(key<root.val): 
                root=root.left
            elif(key>root.val):
                root=root.right
        if not root: return ans.left

        if not root.left:
            if(prev.left==root):
                prev.left=root.right
            else:
                prev.right=root.right
        elif not root.right: 
            if(prev.left==root):
                prev.left=root.left
            else:
                prev.right=root.left
        else:
            temp=root.right
            while(temp.left):
                temp=temp.left
            temp.left=root.left

            if(prev.left==root):
                prev.left=root.right
            else:
                prev.right=root.right
        return ans.left
            

        