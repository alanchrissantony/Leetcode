class Solution:
    def hasSameDigits(self, s: str) -> bool:
        dx = dy = {}
        wl, n=s, len(s)
        for i in range(10):
            j=str(i)
            dx[j],dy[i]=i,j
            
        while n>2:
            ss=""
            for i in range(1, n):
                ss+=dy[(dx[wl[i-1]]+dx[wl[i]])%10]
            wl=ss
            n-=1
        return wl[0]==wl[1]