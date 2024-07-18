from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dict={k:1 for k in nums}
        for i in range(1, len(nums)+1):
            if i not in dict:
                return(i)
        return(i+1)