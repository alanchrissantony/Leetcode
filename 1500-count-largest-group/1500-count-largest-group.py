class Solution:
    def countLargestGroup(self, n: int) -> int:
        dx={}
        dt={}
        for el in range(1,n+1):
            dy=sum(map(int, list(str(el))))
            if dy in dx:
                dx[dy]+=1
            else:
                dx[dy]=1
        for el in dx:
            if dx[el] in dt:
                dt[dx[el]]+=1
            else:
                dt[dx[el]]=1
        return dt[max(dt)]