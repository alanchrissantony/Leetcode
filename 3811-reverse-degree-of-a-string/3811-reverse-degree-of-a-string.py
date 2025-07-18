class Solution:
    def reverseDegree(self, s: str) -> int:
        dt={}
        for idx, el in enumerate(string.ascii_lowercase):
            dt[el]=26-idx
        prd=0
        for idx, el in enumerate(s):
            prd+=dt[el]*(idx+1)
        return prd