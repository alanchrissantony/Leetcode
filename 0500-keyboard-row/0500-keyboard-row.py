class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a=set("qwertyuiop")
        b=set("asdfghjkl")
        c=set("zxcvbnm")
        dx=[]
        for word in words:
            s=set(word.lower())
            if s<=a or s<=b or s<=c:
                dx.append(word)
        return dx