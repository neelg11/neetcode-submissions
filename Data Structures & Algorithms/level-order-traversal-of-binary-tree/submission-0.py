# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack=[[root,0]]
        ans=[]
        while(stack):
            node=stack.pop()
            if(not node[0]): continue
            stack.append([node[0].right,node[1]+1])
            stack.append([node[0].left,node[1]+1])
            if(len(ans)<=node[1]):
                ans.append([])
            ans[node[1]].append(node[0].val)
                
        return ans
