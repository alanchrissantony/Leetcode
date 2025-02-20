class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for el in s:
            if el in t[i:]:
                i=(t[i:].index(el)+1)+i
                print(t[i:])
            else:
                return False
        return True