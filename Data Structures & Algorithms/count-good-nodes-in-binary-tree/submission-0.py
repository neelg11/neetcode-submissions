# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        #stack=[[curr_root, max in this path]]
        stack=[[root,root.val]]
        ans=0
        while(stack):
            node=stack.pop()
            maxinpath=node[1]
            if(node[0].val>=maxinpath):
                maxinpath=node[0].val
                ans+=1
            if(node[0].left):
                stack.append([node[0].left,maxinpath])
            if(node[0].right):
                stack.append([node[0].right,maxinpath])
        return ans