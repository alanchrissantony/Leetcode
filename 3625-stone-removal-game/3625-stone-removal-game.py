class Solution:
    def canAliceWin(self, n: int) -> bool:
        limit=10
        idx=0
        while n>=limit>0:
            n-=limit
            limit-=1
            idx+=1
        return idx%2==1