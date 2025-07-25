class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n=len(s)
        dt={'a':0, 'b':0, 'c':0}
        for el in s:
            dt[el]+=1
        if min(dt.values())<k:
            return -1
        dx=float("inf")
        ldx=0
        for rdx in range(n):
            dt[s[rdx]]-=1
            while min(dt.values())<k:
                dt[s[ldx]]+=1
                ldx+=1
            dx=min(dx, n-(rdx-ldx+1))
        return dx

