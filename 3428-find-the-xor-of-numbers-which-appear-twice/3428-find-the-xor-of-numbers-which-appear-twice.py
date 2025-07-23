class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        dx=set()
        cnt=0
        for el in nums:
            if el in dx:
                cnt^=el
            else:
                dx.add(el)
        return cnt