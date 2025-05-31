class Solution:
    def fib(self, n: int) -> int:
        dx,dy=1,0
        for idx in range(2,n):
            dx,dy=dx+dy,dx
        return dx+dy if n>0 else 0