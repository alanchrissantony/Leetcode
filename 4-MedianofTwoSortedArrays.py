class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums1.extend(nums2)

        def join(left, right):
            i=0
            j=0
            nums1=[]
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    nums1.append(left[i])
                    i+=1
                else:
                    nums1.append(right[j])
                    j+=1
            while i<len(left):
                nums1.append(left[i])
                i+=1
            while j<len(right):
                nums1.append(right[j])
                j+=1
            return nums1

        def merge_sort(nums1):
            if len(nums1)<=1:
                return nums1
            mid=len(nums1)//2
            left=nums1[:mid]
            right=nums1[mid:]
            
            return join(merge_sort(left), merge_sort(right))

        nums1=merge_sort(nums1)

        if len(nums1)%2==0:
            return (nums1[(len(nums1)//2)-1]+nums1[(len(nums1)//2)])/2
        return nums1[(len(nums1)//2)]
