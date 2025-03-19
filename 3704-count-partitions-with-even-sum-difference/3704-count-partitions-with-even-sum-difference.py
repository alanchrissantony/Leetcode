class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        dx,lft,rht=0,0,sum(nums)
        for i in range(len(nums)-1):
            lft+=nums[i]
            rht-=nums[i]
            if (lft-rht)%2==0:
                dx+=1
        return dx

