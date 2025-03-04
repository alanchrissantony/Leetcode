class Solution:
    def hasSameDigits(self, s: str) -> bool:
        dx = {str(i): i for i in range(10)}
        dy = {i: str(i) for i in range(10)}
        wl, n=s, len(s)
        while n>2:
            ss=""
            for i in range(1, n):
                ss+=dy[(dx[wl[i-1]]+dx[wl[i]])%10]
            wl=ss
            n-=1
        return wl[0]==wl[1]