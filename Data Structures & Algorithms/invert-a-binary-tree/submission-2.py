# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        visited=[False]
        stack=[root]
        while(stack):
            curr=stack.pop()
            vis=visited.pop()
            if(curr):
                if(vis):
                    curr.left,curr.right=curr.right,curr.left
                else:
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right) #No need to do right first, anything ok
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)
        return root