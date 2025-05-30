class Solution:
    def maximumTime(self, time: str) -> str:
        dt={0:2, 1:9, 3:5, 4:9}
        for idx, el in enumerate(time):
            if el == "?":
                if idx==1 and time[0]=='2':
                    time=time[:idx]+str(dt[idx]-6)+time[idx+1:]
                elif idx==0 and time[1]!="?" and int(time[1])>3:
                    time=time[:idx]+str(dt[idx]-1)+time[idx+1:]
                else:
                    time=time[:idx]+str(dt[idx])+time[idx+1:]
        return time
