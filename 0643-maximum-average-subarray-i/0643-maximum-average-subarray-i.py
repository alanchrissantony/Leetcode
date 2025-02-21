class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sm=sum(nums[:k])
        mx=sm
        for i in range(k, len(nums)):
            print(sm)
            sm+=nums[i]
            sm-=nums[i-k]
            mx=max(mx, sm) 
        return mx/k