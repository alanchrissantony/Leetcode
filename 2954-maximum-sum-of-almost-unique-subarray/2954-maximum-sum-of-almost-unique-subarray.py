class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        mx=0
        for i in range(len(nums)-k+1):
            dx=nums[i:i+k]
            if len(set(dx))>=m:
                mx=max(mx, sum(dx))
        return mx
            