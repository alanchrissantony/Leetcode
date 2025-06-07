class Solution:
    def smallestNumber(self, n: int) -> int:
        dx='1'*len(bin(n)[2:])
        return int(dx, 2)