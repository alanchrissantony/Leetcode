class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sp=set()
        dp=[]
        for el in nums:
            if el not in sp:
                sp.add(el)
            else:
                dp.append(el)
        return dp