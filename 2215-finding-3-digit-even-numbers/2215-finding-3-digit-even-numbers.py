class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        dt={}
        dx=[]
        for i, el in enumerate(digits):
            if el not in dt and el%2==0:
                dt[str(el)]=digits[:i]+digits[i+1:]
        for el in dt:
            for i,x in enumerate(dt[el]):
                if x==0:
                    continue
                for j,y in enumerate(dt[el]):
                    if i==j:
                        continue
                    z=str(x)+str(y)
                    v=int(z+el)
                    if v not in dx:
                        dx.append(v)
        dx.sort()
        return dx
        