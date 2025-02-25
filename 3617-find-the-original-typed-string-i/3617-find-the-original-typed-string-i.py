class Solution:
    def possibleStringCount(self, word: str) -> int:
        dx=[]
        prev=word[0]
        count=0
        n=len(word)
        for x in range(1,n):
            if word[x]==prev:
                count+=1
            elif count>0:
                dx.append(count)
                count=0
            prev=word[x]
        if count>0:
            dx.append(count)
        return sum(dx)+1
