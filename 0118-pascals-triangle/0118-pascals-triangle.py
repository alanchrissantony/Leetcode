class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp=[[1]]
        for i in range(2, numRows+1):
            dx=[1]
            for j in range(1,i-1):
                dx.append(dp[-1][j]+dp[-1][j-1])
            dx.append(1)
            dp.append(dx)
        return dp