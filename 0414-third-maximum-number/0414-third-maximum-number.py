class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort(reverse=True)
        return nums[2] if len(nums)>2 else nums[0]