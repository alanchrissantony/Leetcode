class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n=len(s)

        if n < 3*k: return -1
        dp=[0]*3

        for char in s:
            dp[ord(char)-ord('a')]+=1

        if min(dp)<k: return -1

        lft=0
        for rgt, char in enumerate(s):
            dp[ord(char)-ord('a')]-=1
            if min(dp)<k:
                dp[ord(s[lft])-ord('a')]+=1
                lft+=1
        return n-(rgt-lft+1)
            



