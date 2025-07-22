class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        dt = {chr(el):idx+1 for idx, el in enumerate(range(ord('a'), ord('h')+1))}
        return((dt[coordinate1[0]]+int(coordinate1[1]))%2 == (dt[coordinate2[0]]+int(coordinate2[1]))%2)