class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m=len(word1), len(word2)
        o=min(n,m)
        s=""
        for x in range(o):
            s+=word1[x]
            s+=word2[x]
        return s+word1[o:]+word2[o:]
            