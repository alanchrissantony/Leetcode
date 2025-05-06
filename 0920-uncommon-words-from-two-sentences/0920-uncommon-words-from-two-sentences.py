class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dy=[]
        dx=s1.split(" ")+s2.split(" ")
        cnt=Counter(dx)
        for el in cnt:
            if cnt[el]<2:
                dy.append(el)
        return dy