class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        lft=[float("inf")]*n
        rgt=[float("inf")]*n
        dp=[0]*n

        dx=float("inf")
        for idx in range(n):
            if s[idx] == c:
                dx=0
                lft[idx]=dx
            else:
                if dx != float("inf"):
                    dx+=1
                    lft[idx]=dx
        
        dx=float("inf")
        for idx in range(n-1, -1, -1):
            if s[idx] == c:
                dx=0
                rgt[idx]=dx
            else:
                if dx != float("inf"):
                    dx+=1
                    rgt[idx]=dx
        for idx in range(n):
            dp[idx]=min(lft[idx], rgt[idx])
        return dp


        