class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        dt={}
        cnt=1
        n=len(nums)
        if n<=1:
            return 1
        for idx in range(1, n):
            if nums[idx]==nums[idx-1]:
                cnt+=1
            else:
                if nums[idx-1] in dt:
                    dt[nums[idx-1]]=max(cnt, dt[nums[idx-1]])
                else:
                    dt[nums[idx-1]]=cnt
                cnt=1
        if nums[idx] in dt:
            dt[nums[idx]]=max(cnt, dt[nums[idx]])
        else:
            dt[nums[idx]]=cnt
        return dt[max(dt)]
        
