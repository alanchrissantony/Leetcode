class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i,n=0,len(s)
        arr=[0]*(n+1)
        for x in range(n):
            if s[x]=='I':
                arr[x]=i
                i+=1
            else:
                arr[x]=n
                n-=1
        arr[-1]=n
        return arr