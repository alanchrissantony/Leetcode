class Solution:
    def minimumChairs(self, s: str) -> int:
        avl=0
        mx=0
        for el in s:
            if el=='E':
                avl+=1
            else:
                avl-=1
            mx=max(mx, avl)
        return mx
            
        