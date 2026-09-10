"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtohead={}
        oldtohead[None]=None
        curr=head
        while(curr):
            oldtohead[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while(curr):
            copy=oldtohead[curr]
            copy.next=oldtohead[curr.next]
            copy.random=oldtohead[curr.random]
            curr=curr.next
        return oldtohead[head]
