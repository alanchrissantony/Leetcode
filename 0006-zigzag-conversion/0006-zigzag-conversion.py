class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        stg=""
        dp=[[] for _ in range(numRows)]
        i=0
        flag=True
        for x in s:
            dp[i].append(x)
            if flag:
                i+=1
            else:
                i-=1
            if i>=numRows-1:
                flag=False
            elif i<=0:
                flag=True

        for x in dp:
            stg+="".join(map(str, x))

        return stg