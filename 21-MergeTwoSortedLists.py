from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        while list1 and list2:
            arr.append(list1.val)
            list1=list1.next
            arr.append(list2.val)
            list2=list2.next
        while list1:
            arr.append(list1.val)
            list1=list1.next
        while list2:
            arr.append(list2.val)
            list2=list2.next

        def join(left, right):
            arr=[]
            i=0
            j=0

            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    arr.append(left[i])
                    i+=1
                else:
                    arr.append(right[j])
                    j+=1
            while i<len(left):
                arr.append(left[i])
                i+=1
            while j<len(right):
                arr.append(right[j])
                j+=1
            return arr
                
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            mid=len(arr)//2
            left=arr[:mid]
            right=arr[mid:]

            return join(merge_sort(left), merge_sort(right))

        arr=merge_sort(arr)

        res=ListNode()
        i=0
        while i<len(arr):
            current=res
            while current.next:
                current=current.next
            current.next=ListNode(arr[i])
            i+=1
        return res.next
