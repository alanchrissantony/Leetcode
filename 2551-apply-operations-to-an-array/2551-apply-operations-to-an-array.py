class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        cnt=0
        i,n=1,len(nums)
        while i<n:
            if nums[i-1]==0:
                cnt+=1
                del nums[i-1]
                n-=1
                continue
            elif nums[i]==nums[i-1]:
                nums[i-1]*=2
                del nums[i]
                cnt+=1
                n-=1
            i+=1
        return nums+[0]*cnt