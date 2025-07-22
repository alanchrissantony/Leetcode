class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        dt=set()
        cx=mx=0
        left=0
        for right in range(n):
            while nums[right] in dt:
                cx-=nums[left]
                dt.remove(nums[left])
                left+=1
            dt.add(nums[right])
            cx+=nums[right]
            mx=max(mx, cx)
        return mx
            
            
        
        
                