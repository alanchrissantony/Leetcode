class Solution:
    def possibleStringCount(self, word: str) -> int:
        count=1
        for x in range(1,len(word)):
            if word[x]==word[x-1]:count+=1
        return count
