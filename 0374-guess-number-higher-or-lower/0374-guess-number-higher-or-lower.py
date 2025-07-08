# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        def search(start, end):
            mid=(start+end)//2
            dx=guess(mid)
            if dx==1:
                return search(mid+1, end)
            elif dx==-1:
                return search(start, mid-1)
            else:
                return mid
        return search(0, n)