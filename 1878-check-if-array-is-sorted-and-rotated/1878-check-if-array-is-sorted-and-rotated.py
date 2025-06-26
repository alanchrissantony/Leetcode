class Solution:
    def check(self, nums: List[int]) -> bool:
        dx=0
        n=len(nums)
        for idx in range(n):
            if nums[idx]>nums[(idx+1) % n]:
                dx+=1
            if dx>1:
                return False
        return True
