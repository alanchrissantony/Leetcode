class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        dx=[first]
        for i in encoded:
            dx.append(i^dx[-1])
        return dx