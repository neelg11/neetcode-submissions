#iteration
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        decision_stack=[[[],0]]
        n=len(nums)
        res=[]
        while(decision_stack):
            curr=decision_stack.pop()
            curr_set=curr[0]
            idx=curr[1]
            if(idx>=n):
                res.append(curr_set)
            else:
                decision_stack.append([curr_set.copy(),idx+1]) #if you pass just curr_set then the ref goes not the copy
                curr_set.append(nums[idx])
                decision_stack.append([curr_set,idx+1])
        return res


        