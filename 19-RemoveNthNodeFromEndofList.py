from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        count=0
        while current:
            count+=1
            current=current.next

        target=count-n

        current=head
        i=0
        while current:
            if target==0:
                if current.next:
                    head=current.next
                    return head
                else:
                    return None
            i+=1
            if i==target:
                if current.next.next:
                    current.next = current.next.next
                else:
                    current.next=None
            current=current.next

        return head
