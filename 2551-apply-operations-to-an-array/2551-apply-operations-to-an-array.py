class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for idx in range(n-1):
            if nums[idx]==nums[idx+1]:
                nums[idx]*=2
                nums[idx+1]=0
        lft=0
        for rgt in range(n):
            if nums[rgt]!=0:
                nums[lft], nums[rgt] = nums[rgt], nums[lft]
                lft+=1
        return nums