class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        dx=[]
        for i, el in enumerate(number):
            if el == digit:
                dx.append(number[:i]+number[i+1:])
            continue
        return max(dx)