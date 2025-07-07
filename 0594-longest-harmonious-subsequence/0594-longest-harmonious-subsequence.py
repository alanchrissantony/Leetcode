class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dt=Counter(nums)
        mx=0
        for el in dt:
            if el+1 in dt and el-1 in dt:
                mx=max(mx, dt[el]+max(dt[el+1], dt[el-1]))
            elif el+1 in dt:
                mx=max(mx, dt[el]+dt[el+1])
            elif el-1 in dt:
                mx=max(mx, dt[el]+dt[el-1])
        return mx

        

            
