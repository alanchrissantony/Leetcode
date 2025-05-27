class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        idx=0
        while idx<n:
            if arr[idx]==0:
                arr.insert(idx,0)
                arr.pop()
                idx+=1
            idx+=1
        return arr