class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        dx=[0]*(len(encoded)+1)
        dx[0]=first
        for i, el in enumerate(encoded):
            dx[i+1]=el^dx[i]
        return dx