class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=nums[0]
        current=nums[0]
        n=len(nums)
        for i in range(1, n):
            current=max(nums[i], current+nums[i])
            sum=max(sum, current)
        return sum