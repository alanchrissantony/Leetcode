class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for idx in range(1,len(nums)):
            if nums[i]!=0:
                i+=1
            if nums[i]==0 and nums[idx]!=0:
                nums[i],nums[idx]=nums[idx],nums[i]
                i+=1
        return nums
