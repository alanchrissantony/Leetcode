class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dx=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dy=dict(zip(string.ascii_lowercase, dx))
        sy={}
    
        for word in words:
            rst=""
            for el in word:
                rst+=dy[el]
            sy[rst]=1
        return len(sy)