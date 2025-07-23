class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n=len(arr1)
        left=0
        for el in arr2:
            for right in range(left+1,n):
                if arr1[left]!=arr1[right] and arr1[right]==el:
                    arr1[left], arr1[right] = arr1[right], arr1[left]
                    left+=1
                    right+=1
                if arr1[left]==el:
                    left+=1
                if right<n and arr1[right]!=el:
                    right+=1
        for ldx in range(left, n-1):
            for rdx in range(ldx+1, n):
                if arr1[ldx]>arr1[rdx]:
                   arr1[ldx], arr1[rdx] = arr1[rdx], arr1[ldx]
        return arr1
