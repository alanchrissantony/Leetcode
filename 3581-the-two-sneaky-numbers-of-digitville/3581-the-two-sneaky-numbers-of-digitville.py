class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sp=[]
        dp=[]
        for el in nums:
            if el not in sp:
                sp.append(el)
            else:
                dp.append(el)
        return dp