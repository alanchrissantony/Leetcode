class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dx=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dy={}
        sy={}
    
        for i, el in enumerate(string.ascii_lowercase):
            dy[el]=dx[i]
        for word in words:
            rst=""
            for el in word:
                rst+=dy[el]
            sy[rst]=1
        return len(sy)