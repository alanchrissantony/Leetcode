class Solution:
    def findLatestTime(self, s: str) -> str:
        dt={0:1, 1:9, 3:5, 4:9}
        for idx, el in enumerate(s):
            if el=='?':
                if idx==0 and s[idx+1]!='?' and int(s[idx+1])>1:
                    s=s[:idx]+str(dt[idx]-1)+s[idx+1:]
                elif idx==1 and int(s[idx-1])>0:
                    s=s[:idx]+str(dt[idx]-8)+s[idx+1:]
                else:
                    s=s[:idx]+str(dt[idx])+s[idx+1:]
        return s