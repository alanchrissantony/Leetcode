class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        while i<n:
            if(sum(nums[:i]) == sum(nums[i+1:])):
                return i
            i+=1
        return -1