class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sarr=[]
        tarr=[]
        for i in range(len(s)):
            sarr.append(s[i:].count(s[i]))
            sarr.append(s[::-1][i:].count(s[i]))
            tarr.append(t[i:].count(t[i]))
            tarr.append(t[::-1][i:].count(t[i]))
            
        return(sarr==tarr)