class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        mx=float("-inf")
        dx=-1
        for idx, el in enumerate(arr):
            if el>mx:
                mx=el
                dx=idx
        return dx