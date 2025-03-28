class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        for i in range(1,n):
            dp[i]=max(nums[i]+dp[i-2], dp[i-1])
        return dp[n-1]