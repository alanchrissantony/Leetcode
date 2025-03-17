class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dx=Counter(nums)
        for el in dx:
            if dx[el]%2!=0:
                return False
        return True