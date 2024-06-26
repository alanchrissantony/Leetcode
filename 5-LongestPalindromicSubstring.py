class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ""
        for i in range(len(s)):
            res=""
            for j in range(i,len(s)):
                res+=s[j]
                if res == res[::-1] and len(res)>len(out):
                    out = res
        return(out)