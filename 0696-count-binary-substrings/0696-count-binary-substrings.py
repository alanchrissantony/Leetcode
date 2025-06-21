class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        previous=0
        current=1
        count=0
        for idx in range(1, len(s)):
            if s[idx]==s[idx-1]:
                current+=1
            else:
                count+=min(previous, current)
                previous=current
                current=1
        count+=min(previous, current)
        return count