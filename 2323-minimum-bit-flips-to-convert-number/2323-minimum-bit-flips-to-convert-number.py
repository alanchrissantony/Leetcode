class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cnt=0
        start,goal=bin(start)[2:],bin(goal)[2:]
        start=max(0, len(goal)-len(start))*"0"+start
        goal=max(0, len(start)-len(goal))*"0"+goal
        for idx in range(len(start)):
            if start[idx]!=goal[idx]:
                cnt+=1
        return cnt