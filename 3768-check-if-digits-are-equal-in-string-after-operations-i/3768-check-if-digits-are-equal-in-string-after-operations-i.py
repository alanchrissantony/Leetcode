class Solution:
    def hasSameDigits(self, s: str) -> bool:
        wl=s
        while len(wl)>2:
            ss=""
            for i in range(1, len(wl)):
                ss+=str((int(wl[i-1])+int(wl[i]))%10)
            wl=ss
        return wl[0]==wl[1]