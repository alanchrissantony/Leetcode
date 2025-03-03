class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel={'a', 'e', 'i', 'o', 'u'}
        return len(set(s).intersection(vowel))>0