class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        n,m=len(players),len(trainers)
        i=j=dx=0
        players.sort()
        trainers.sort()
        while i<n and j<m:
            if players[i]>trainers[j]:
                j+=1
            else:
                i+=1
                j+=1
                dx+=1
        return dx
        