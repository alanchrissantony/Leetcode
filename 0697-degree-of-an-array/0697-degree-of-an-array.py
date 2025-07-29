class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        ct=dict(reversed(sorted(Counter(nums).items(), key=lambda item:item[1])))
        dp=[]
        mx=float("-inf")
        for el in ct:
            if ct[el]>=mx:
                mx=ct[el]
                dp.append(el)
        dt={}
        for idx, num in enumerate(nums):
            if num in dt:
                dt[num][1]=idx
            else:
                dt[num]=[idx,idx]

        for idx,el in enumerate(dp):
            dp[idx]=dt[el][1]-dt[el][0]
        return min(dp)+1

        
        