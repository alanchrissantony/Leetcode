class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt=0
        for el in patterns:
            if el in word:
                cnt+=1
        return cnt