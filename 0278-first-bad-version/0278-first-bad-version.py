# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        def search(start, end):
            if(start+1>=end):
                return end
            mid=(start+end)//2
            if isBadVersion(mid):
                return search(start, mid)
            else:
                return search(mid, end)
        return search(0, n)
            