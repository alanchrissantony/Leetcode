class Solution:
    def makeFancyString(self, s: str) -> str:
        dx=s[:2]
        n=len(dx)
        for idx in range(2,len(s)):
            if n>1 and dx[-1]==dx[-2]==s[idx]:
                continue
            else:
                dx+=s[idx]
        return dx

