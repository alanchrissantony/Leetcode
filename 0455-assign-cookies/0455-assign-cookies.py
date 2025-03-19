class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n=len(g)
        m=len(s)
        g.sort()
        s.sort()
        i=j=dx=0
        while i<n and j<m:
            if g[i]>s[j]:
                j+=1
            else:
                i+=1
                j+=1
                dx+=1
        return dx