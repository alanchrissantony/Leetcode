class Solution:
    def freqAlphabets(self, s: str) -> str:
        dx=dict(zip(map(str, range(1, 27)), string.ascii_lowercase))
        i,k,n=0,2,len(s)
        dp=""
        while i<n:
            if i+k<n and s[i+k]=="#":
                dp+=dx[s[i:i+k]]
                i+=k
            else:
                dp+=dx[s[i]]
            i+=1
        return dp
        
