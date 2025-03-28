class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for x in count:
            if count[x]==1:
                return x
        return -1