# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(self,p,q):
            stack_p=[p]
            stack_q=[q]
            while(stack_p and stack_q):
                cur_p,cur_q=stack_p.pop(),stack_q.pop()
                if(cur_p and cur_q and cur_p.val == cur_q.val):
                    stack_p.append(cur_p.left)
                    stack_p.append(cur_p.right)
                    stack_q.append(cur_q.left)
                    stack_q.append(cur_q.right)
                elif(cur_p or cur_q):
                    return False
            if(stack_p or stack_q): return False
            return True
        if (not subRoot): return True
        if (not root): return False
        stack=[root]
        while(stack):
            node=stack.pop()
            if(sametree(self,node,subRoot)): return True
            if(node.left): stack.append(node.left)
            if(node.right): stack.append(node.right)
        return False
            
        
        