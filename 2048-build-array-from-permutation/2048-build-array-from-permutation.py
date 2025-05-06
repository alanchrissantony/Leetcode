class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        dp=[0]*len(nums)
        for i, el in enumerate(nums):
            dp[i]=nums[el]
        return dp
        