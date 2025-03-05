class Solution:
    def firstUniqChar(self, s: str) -> int:
        sx=set(list(s))
        idx=len(s)
        flag=False
        for el in sx:
            if s.count(el)<2 and s.index(el)<idx:
                idx=s.index(el)
                flag=True
        return idx if flag else -1