class Solution:
    def sumZero(self, n: int) -> List[int]:
        dp=[]
        for idx in reversed(range(ceil(n/2))):
            if idx<1 and n%2==1:
                dp.extend([idx])
            else:
                dp.extend([-idx-1, idx+1])

        return dp
