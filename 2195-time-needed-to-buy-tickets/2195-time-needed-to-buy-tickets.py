class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt=0
        for idx in range(len(tickets)):
            if idx<=k:
                cnt+=min(tickets[idx], tickets[k])
            else:
                cnt+=min(tickets[idx], tickets[k]-1)
        return cnt
