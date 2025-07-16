class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(fruits)
        f_idx=b_idx=k=0
        while f_idx<n-k:
            b_idx=0
            while b_idx<n-k:
                if baskets[b_idx]>=fruits[f_idx]:
                    del fruits[f_idx]
                    del baskets[b_idx]
                    k+=1
                    f_idx-=1
                    break
                b_idx+=1
            f_idx+=1

        return len(baskets)

