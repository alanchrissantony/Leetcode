class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dx=Counter(ransomNote)
        dy=Counter(magazine)
        return dx<=dy