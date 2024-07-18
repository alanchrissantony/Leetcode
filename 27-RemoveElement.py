from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while i<len(nums):
            if nums[i]==val:
                del nums[i]
                i=i-1
            i=i+1
                
        return len(nums)