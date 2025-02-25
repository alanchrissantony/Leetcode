class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dx={'a':2,'b':3,'c':3,'d':2,'e':1,'f':2,'g':2,'h':2,'i':1,'j':2,'k':2,'l':2,'m':3,'n':3,'o':1,'p':1,'q':1,'r':1,'s':2,'t':1,'u':1,'v':3,'w':1,'x':3,'y':1,'z':3}
        dp=[]
        for word in words:
            wrd=word.lower()
            dy=dx[wrd[0]]
            flag=True
            for el in wrd:
                if dx[el]!=dy:
                    flag=False
                    break
            if flag:
                dp.append(word)
        return dp