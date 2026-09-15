class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stack=[root]
        visited=[False]
        while(stack):
            curr=stack.pop()
            vis=visited.pop()
            if(vis):
                res.append(curr.val)
            elif(curr):
                stack.append(curr)
                visited.append(True)

                if(curr.right):
                    stack.append(curr.right)
                    visited.append(False)

                if(curr.left):
                    stack.append(curr.left)
                    visited.append(False)
        return res