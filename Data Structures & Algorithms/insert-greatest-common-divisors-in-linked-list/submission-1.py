# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
         
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a

        itr=head
        while(itr and itr.next):
            a, b = itr.val, itr.next.val
            g = gcd(a,b)
            temp = itr.next
            itr.next = ListNode(g, temp)
            itr = itr.next.next
        return head
