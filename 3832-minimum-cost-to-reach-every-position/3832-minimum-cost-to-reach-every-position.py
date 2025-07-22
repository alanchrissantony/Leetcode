class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        dp=[]
        mn=cost[0]
        for el in cost:
            if el<mn:
                mn=el
            dp.append(mn)
        return dp