class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or=0
        n=len(nums)
        for el in nums:
            max_or|=el
        def helper(i, curr_or):
            nonlocal n, max_or
            if i==n:
                return 1 if curr_or==max_or else 0
            return (helper(i+1, curr_or)+helper(i+1, curr_or|nums[i]))

        return helper(0,0)