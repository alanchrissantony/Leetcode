class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        dx=0
        for i in range(len(nums)):
            s=set()
            for j in range(i, len(nums)):
                s.add(nums[j])
                dist=len(s)
                dx+=dist**2
        return dx