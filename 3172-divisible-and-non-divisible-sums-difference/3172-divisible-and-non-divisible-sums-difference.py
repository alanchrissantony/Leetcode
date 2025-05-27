class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        dn,dm=0,0
        for i in range(1, n+1):
            if i%m==0:
                dm+=i
            else:
                dn+=i
        return dn-dm
