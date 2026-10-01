# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr=head
        while(itr and itr.next):
            a, b = itr.val, itr.next.val
            g = math.gcd(a,b)
            temp = itr.next
            itr.next = ListNode(g, temp)
            itr = itr.next.next
        return head
