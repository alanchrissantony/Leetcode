class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sm=0
        for char in str(x):
            sm+=int(char)
        return sm if x%sm==0 else -1