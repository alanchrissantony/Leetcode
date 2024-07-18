from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        position=None
        val=nums[0]
        if target in nums:
            for i in range(len(nums)):
                if nums[i]==target:
                    position=i
                    break
        elif target<nums[len(nums)-1]:
            for i in range(len(nums)):
                if target<nums[i]:
                    nums.insert(i, target)
                    position=i
                    break
        else:
            nums.insert(len(nums), target)
            position=len(nums)-1
        return position