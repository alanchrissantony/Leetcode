class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dx={0:[1], 1:[0]}
        dy={0:[], 1:[]}
        n=len(groups)
        for idx in range(n):
            if groups[idx]!=dx[0][-1]:
                dx[0].append(groups[idx])
                dy[0].append(words[idx])
            if groups[idx]!=dx[1][-1]:
                dx[1].append(groups[idx])
                dy[1].append(words[idx])
        if len(dx[0])>len(dx[1]):
            return dy[0]
        return dy[1]
            
        
                
