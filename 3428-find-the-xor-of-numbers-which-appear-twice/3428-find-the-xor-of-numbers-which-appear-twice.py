class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        dx=Counter(nums)
        cnt=0
        for el in dx:
            if dx[el]>1:
                cnt^=el
        return cnt