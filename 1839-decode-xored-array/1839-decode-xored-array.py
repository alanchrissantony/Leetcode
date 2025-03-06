class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        dx=[first]+[0]*len(encoded)
        for i, el in enumerate(encoded):
            dx[i+1]=el^dx[i]
        return dx