class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)):
            nums[x]=nums[x]%2
        nums.sort()
        return nums