class Solution:
    def check(self, nums: List[int]) -> bool:
        srt=sorted(nums)
        if srt==nums:True

        for i in range(len(nums)):
            if nums[i:]+nums[:i]==srt:return True
        return False