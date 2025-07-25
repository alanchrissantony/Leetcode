class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mx=max(nums)
        for num in nums:
            if num>=0:
                mx=0
                break
        dp=set()
        for num in nums:
            if num not in dp and num>0:
                dp.add(num)
                mx+=num
        return mx