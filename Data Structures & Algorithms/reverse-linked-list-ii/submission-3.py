# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        l_itr = r_itr = dummy
        count=right-left+1
        prev=None
        while(left or right):
            if(left):
                prev=l_itr
                l_itr=l_itr.next
                left-=1
            r_itr=r_itr.next
            right-=1
        prev.next=r_itr
        prev=r_itr.next
        
        while(count):
            tmp=l_itr.next
            l_itr.next=prev
            prev=l_itr
            l_itr=tmp
            count-=1

        return dummy.next
        

        
        