class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        dt = {}
        mx=0
        ldx=0
        for rdx, char in enumerate(s):
            if char not in dt:
                dt[char]=1
            else:
                dt[char]+=1
                while max(dt.values())>2:
                    dt[s[ldx]]-=1
                    ldx+=1
            mx=max(mx, (rdx-ldx+1))
        return mx

