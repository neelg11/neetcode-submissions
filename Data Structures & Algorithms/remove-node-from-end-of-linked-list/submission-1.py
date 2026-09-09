# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itr=head
        count=n
        while(count):
            itr=itr.next
            count-=1
        del_itr=head
        prev=None
        while(itr):
            itr=itr.next
            prev=del_itr
            del_itr=del_itr.next
        if(prev):
            prev.next=del_itr.next
            return head
        return del_itr.next
        
        