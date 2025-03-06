class Solution:
    def equalFrequency(self, word: str) -> bool:
        dx=Counter(word)
        dy=list(dx.values())
        for i in range(len(dy)):
            dy[i]-=1
            sx=len(set(dy))
            if sx==1:
                return True
            elif sx==2 and dy[i]==0:
                return True
            dy[i]+=1
        return False
        
