class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dp=[]
        for el in grid:
            dp=[*dp, *el]
        dy=0
        for i in range(1, len(dp)+1):
            if i not in dp:
                dy=i
            elif dp.count(i)>1:
                dx=i
        return [dx, dy]