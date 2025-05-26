class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n,m=len(s), len(goal)
        if n==m:
            for i in range(n):
                if s[:i] in goal and s[i:] in goal:
                    return True
        return False