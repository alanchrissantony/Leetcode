class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt=0
        dx={}
        vowel='aeiou'
        vx=cx=0
        for el in s:
            if el in vowel:
                if el in dx:
                    dx[el]+=1
                else:
                    dx[el]=1
                vx=max(vx, dx[el])
            else:
                if el in dx:
                    dx[el]+=1
                else:
                    dx[el]=1
                cx=max(cx, dx[el])
        return vx+cx
