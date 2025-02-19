class Solution:
    def findValidPair(self, s: str) -> str:
        for i in range(len(s)-1):
            if s.count(s[i])==int(s[i]) and s.count(s[i+1])==int(s[i+1]) and s[i]!=s[i+1]:
                return s[i]+s[i+1]
        return ""

