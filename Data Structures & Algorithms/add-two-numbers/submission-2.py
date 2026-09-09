# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        ans=dummy
        sum,carry=0,0
        while(l1 or l2):
            sum=0
            if(l1):
                sum+=l1.val
                l1=l1.next
            if(l2):
                sum+=l2.val
                l2=l2.next
            print(sum)
            print(carry)
            dummy.next=ListNode((sum+carry)%10)
            carry=(sum+carry)//10
            dummy=dummy.next
            
        if(carry):
            dummy.next=ListNode(carry)
        return ans.next
        