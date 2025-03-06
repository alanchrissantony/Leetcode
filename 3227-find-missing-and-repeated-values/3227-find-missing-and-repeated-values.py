class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dp=[]
        for el in grid:
            dp=[*dp, *el]
        cnt=Counter(dp)
        for i in range(1, len(dp)+1):
            if i not in cnt:
                dy=i
            elif cnt[i]>1:
                dx=i
        return [dx, dy]