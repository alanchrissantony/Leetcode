class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        zy=0
        dx=len(set(nums))
        dy=len(nums)
        while dx!=dy:
            nums=nums[3:]
            dx=len(set(nums))
            dy=len(nums)
            zy+=1
        return zy