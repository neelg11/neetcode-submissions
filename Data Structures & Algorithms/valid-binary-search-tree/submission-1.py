# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack=[[root,-1000000001,1000000001]]
        while(stack):
            node=stack.pop() #node[0] is the node, node[1] is min limit, node[2] is max limit
            if(node[0].val<=node[1] or node[0].val>=node[2]):
                return False
            if(node[0].left):
                stack.append([node[0].left,node[1],node[0].val])#keep min limit same, update max limit
            if(node[0].right):
                stack.append([node[0].right,node[0].val,node[2]])#update min limit, keep min limit same

        return True