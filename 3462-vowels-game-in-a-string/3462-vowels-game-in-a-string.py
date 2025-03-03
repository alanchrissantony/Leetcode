class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel={'a', 'e', 'i', 'o', 'u'}
        cnt=0
        for el in s:
            if el in vowel:
                cnt+=1
        return cnt>0 and cnt%1==0