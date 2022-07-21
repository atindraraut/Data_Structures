# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        lprev,current = dummy,head
        for i in range(left-1):
            lprev,current = current,current.next
        prev = None
        for i in range((right-left)+1):
            tempNext = current.next
            current.next =prev
            prev,current = current,tempNext
            
        lprev.next.next = current
        lprev.next = prev
        print(dummy.next)  
var = [1,2,3,4,5]
for i in var:
    head = ListNode(i)
Solution.reverseBetween(head,2,4)