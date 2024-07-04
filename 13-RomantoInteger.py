class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        count=0
        dict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        for i in s:
            res=res+dict[i]
            if(count>0 and pre<dict[i]):
                res=res-pre*2
            pre=dict[i]
            count=count+1
        return res