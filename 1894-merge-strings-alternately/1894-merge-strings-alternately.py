class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m=len(word1), len(word2)
        o=max(n,m)
        s=""
        for x in range(o):
            if x<n:
                s+=word1[x]
            if x<m:
                s+=word2[x]
        return s
            