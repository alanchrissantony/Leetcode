# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current=head
        arr=[]
        while current:
            arr.append(current.val)
            current=current.next

        num=[]
        i=0
        while i<len(arr):
            if i%k==0:
                num.extend(arr[len(num):i][::-1])
            i+=1
        if i%k==0:
            num.extend(arr[len(num):i][::-1])
        else:
            num.extend(arr[len(num):i])

        current=head
        i=0
        while current:
            current.val=num[i]
            current=current.next
            i+=1
        return head