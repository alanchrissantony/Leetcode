from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        res=""
        while i<len(strs[0]):
            res+=strs[0][i]
            j=1
            while j<len(strs):
                if res!=strs[j][:len(res)]:
                    return res[:-1]
                j+=1
            i+=1
        return strs[0]