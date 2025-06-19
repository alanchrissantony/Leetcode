class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        dp=[str(x) for x in range(1,n+1)]
        dp.sort()
        dp=[int(x) for x in dp]
        return dp