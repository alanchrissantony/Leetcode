class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt=0
        for ldx in arr1:
            flag=True
            for rdx in arr2:
                if abs(ldx-rdx)<=d:
                    flag=False
                    break
            if flag:
                cnt+=1
        return cnt