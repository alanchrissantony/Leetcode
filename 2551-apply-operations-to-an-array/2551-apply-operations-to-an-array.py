class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for idx in range(n-1):
            if nums[idx]==nums[idx+1]:
                nums[idx]*=2
                nums[idx+1]=0
        dx=idx=0
        while idx<n:
            if nums[idx]==0:
                dx+=1
                del nums[idx]
                n-=1
            else:
                idx+=1
        return nums+[0]*dx