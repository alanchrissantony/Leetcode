class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        flag=True
        m=len(grid)
        for i in range(m):
            flag=True
            n=len(grid[i])
            for j in range(n):
                if i<m-1 and grid[i][j] != grid[i + 1][j]:
                    flag=False
                    break
                if j<n-1 and grid[i][j] == grid[i][j + 1]:
                    flag=False
                    break
            if not flag:
                break
        return flag