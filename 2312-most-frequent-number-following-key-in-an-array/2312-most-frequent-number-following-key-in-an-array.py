class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        n=len(nums)
        dx={}
        mx,nx=-1,-1
        for idx, el in enumerate(nums):
            if el == key and idx<n-1:
                nxt=nums[idx+1]
                if nxt in dx:
                    dx[nxt]+=1
                else:
                    dx[nxt]=1
                if dx[nxt]>mx:
                    mx=dx[nxt]
                    nx=nxt
        return nx
        