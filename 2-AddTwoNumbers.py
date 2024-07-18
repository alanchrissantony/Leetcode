from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_sum = ""
        l2_sum = ""
        current = l1
        while current or l2:
            if current:
                l1_sum+=str(current.val)
                current = current.next
            if l2:
                l2_sum+=str(l2.val)
                l2 = l2.next
        s=(str(int(l1_sum[::-1]) + int(l2_sum[::-1]))[::-1])
        print(s)
        current = l1

        result=ListNode()
        i=0
        while i<len(s):
            current=result
            
            while current.next:
                current = current.next
            current.next = ListNode(s[i])
            i+=1
        return result.next