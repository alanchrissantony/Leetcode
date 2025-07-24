class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        sp=set()
        for idx, el in enumerate(s):
            if el == c:
                sp.add(idx+1)
        dp=[0]*len(s)
        for inx, el in enumerate(s):
            mn=float('inf')
            for it in sp:
                mn=min(mn, abs(it-(inx+1)))
            dp[inx]=mn
        return dp
        