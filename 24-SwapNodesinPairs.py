from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        while current:
            if current.next:
                temp=current.val
                current.val=current.next.val
                current.next.val=temp
                current=current.next.next
            else:
                current=current.next

        return head