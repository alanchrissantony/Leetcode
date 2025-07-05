class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt=Counter(arr)
        mx=-1
        for el in cnt:
            if el == cnt[el] and el>mx:
                mx=el
        return mx