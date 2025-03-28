class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        dp = s.split(' ')[::-1]
        i=0
        while '' in dp and i<len(dp):
            if dp[i] == '':
                del dp[i]
            else:
                i+=1
        x = ' '.join(dp)
        return(x)