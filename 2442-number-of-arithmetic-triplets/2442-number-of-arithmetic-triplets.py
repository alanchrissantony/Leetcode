class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n=len(nums)
        cnt=0
        for ldx in range(n):
            if nums[ldx]-diff in nums and nums[ldx]-diff*2 in nums:
                cnt+=1
        return cnt