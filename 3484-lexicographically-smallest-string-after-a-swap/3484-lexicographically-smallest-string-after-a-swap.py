class Solution:
    def getSmallestString(self, s: str) -> str:
        for i in range(1, len(s)):
            dx=int(s[i])
            dy=int(s[i-1])
            if dx<dy and dx%2==dy%2:
                return s[:i-1]+s[i]+s[i-1]+s[i+1:]
        return s