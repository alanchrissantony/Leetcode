class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""
        arr = []
        if len(s) == 1:
            return(1)
        i = 0
        a = 1
        while i < len(s):
            if s[i] in res:
                arr.append(len(res))
                if s[i-1] != s[i]:
                    i = a
                    a += 1
                res = "" 
            res += s[i]
            i += 1
        arr.append(len(res))
        return(max(arr))