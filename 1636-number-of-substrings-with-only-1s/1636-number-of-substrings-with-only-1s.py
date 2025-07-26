class Solution:
    def numSub(self, s: str) -> int:
        sm=0
        i=0
        for el in s:
            if el=='1':
                i+=1
                sm+=i
            else:
                i=0
        mod = 10**9+7
        return sm % mod