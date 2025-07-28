class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or=0
        dp=defaultdict(int)
        dp[0]=1
        for num in nums:
            dx=deepcopy(dp)
            for curr_or, cnt in dp.items():
                dx[curr_or|num]+=cnt
            dp=dx
            max_or|=num
        return dp[max_or]