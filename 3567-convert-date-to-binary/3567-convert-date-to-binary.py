class Solution:
    def convertDateToBinary(self, date: str) -> str:
        dx=date.split('-')
        for i, el in enumerate(dx):
            dx[i]=bin(int(el))[2:]
        return "-".join(dx)
        
        