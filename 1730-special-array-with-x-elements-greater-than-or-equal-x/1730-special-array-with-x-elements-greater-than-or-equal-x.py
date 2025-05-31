class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n=len(nums)
        for idx in range(1,n+1):
            cnt=0
            for el in nums:
                if el>=idx:
                    cnt+=1
            if cnt==idx:
                return idx
        return -1
