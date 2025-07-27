class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cnt=0
        ldx=0
        curr=1
        for rdx in range(2, len(nums)):
            if (nums[curr]-nums[ldx])*(nums[curr]-nums[rdx])>0:
                cnt+=1
                ldx=curr
            curr+=1
        return cnt
            
            
            
            