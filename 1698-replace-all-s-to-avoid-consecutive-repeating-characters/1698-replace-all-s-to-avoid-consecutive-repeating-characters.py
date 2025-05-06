class Solution:
    def modifyString(self, s: str) -> str:
        char="abc"
        for i, el in enumerate(s):
            if el=='?':
                for j, alp in enumerate(char):
                    if i>0 and alp in s[i-1] or i<len(s)-1 and alp in s[i+1]:
                        continue
                    s=s[:i]+alp+s[i+1:]
        return s