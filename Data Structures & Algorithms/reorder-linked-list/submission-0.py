# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head, head.next
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        itr=slow.next #slow stopped at the last node of first half
        slow.next=None #cutting connection of the two half
        prev=None
        while(itr): # reverse the 2nd half
            tmp=itr.next
            itr.next=prev
            prev=itr
            itr=tmp
        
        first,second=head,prev  #prev is at last node, itr is at None
        while(first and second):
            tmp1,tmp2=first.next, second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
