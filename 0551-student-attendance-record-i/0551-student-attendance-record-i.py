class Solution:
    def checkRecord(self, s: str) -> bool:
        flag=True
        a=l=0
        for el in s:
            if el == "A":
                l=0
                a+=1
            elif el == "L":
                l+=1
            else:
                l=0
            if a>1 or l>2:
                flag=False
        return flag