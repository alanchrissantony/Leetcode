class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt=0
        for el in nums:
            cnt+=min(el%3, 3-el%3)
        return cnt