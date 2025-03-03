class Solution:
    def hasSameDigits(self, s: str) -> bool:
        wl, n=s, len(s)
        while n>2:
            ss=""
            for i in range(1, n):
                ss+=str((int(wl[i-1])+int(wl[i]))%10)
            wl=ss
            n-=1
        return wl[0]==wl[1]