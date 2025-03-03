class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel=frozenset("aeiou")
        return not vowel.isdisjoint(s)