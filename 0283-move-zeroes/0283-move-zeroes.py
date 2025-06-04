class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for idx in range(len(nums)):
            if nums[idx]!=0:
                nums[i],nums[idx]=nums[idx],nums[i]
                i+=1
        return nums
