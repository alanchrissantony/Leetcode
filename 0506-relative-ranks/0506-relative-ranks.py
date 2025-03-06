class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dx=["Gold Medal","Silver Medal","Bronze Medal"]
        dy=dict(sorted({el:idx for idx, el in enumerate(score)}.items(), key=lambda item: item[0], reverse=True))
        n=1    
        for x in dy:
            if n<4:
                dy[x]=dx.pop(0)   
            else:
                dy[x]=str(n)
            n+=1
        for i, el in enumerate(score):
            score[i]=dy[el]
        return score