class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        mx=float("-inf")
        dx=-1
        for idx, num in enumerate(nums):
            if num>mx:
                mx=num
                dx=idx
        return dx
