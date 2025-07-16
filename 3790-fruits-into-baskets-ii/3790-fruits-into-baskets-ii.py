class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unp=len(baskets)

        for fruit in fruits:
            for basket in baskets:
                if basket>=fruit:
                  baskets.remove(basket)
                  unp-=1
                  break
        return unp


