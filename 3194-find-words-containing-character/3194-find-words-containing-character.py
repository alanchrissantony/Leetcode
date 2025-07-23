class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        dp=[]
        for idx, word in enumerate(words):
            if x in word:
                dp.append(idx)
        return dp