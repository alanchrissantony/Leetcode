from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        i=0
        while i<len(strs):
            j="".join(sorted(strs[i]))
            if j in dict:
                dict[j].append(strs[i])
            else:
                dict[j]=[strs[i]]
            i+=1
        arr=[]
        for i in dict:
            arr.append(dict[i])
        return arr
