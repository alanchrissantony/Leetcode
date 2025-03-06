class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt=0
        for i in range(1, n+1):
            n-=i
            if n>=0:
                cnt+=1
            else:
                break
        return cnt