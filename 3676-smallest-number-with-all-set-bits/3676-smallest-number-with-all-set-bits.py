class Solution:
    def smallestNumber(self, n: int) -> int:
        for idx in range(n,n*2):
            if set(bin(idx)[2:])=={'1'}:
                return idx
        return -1