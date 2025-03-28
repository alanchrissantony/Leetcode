class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        dx=0
        for num in nums:
            dx|=num
        return dx*(1<<(len(nums)-1))
        
