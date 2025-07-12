class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        dp=[]
        n=len(nums)
        if n>0:
            idx=nums[0]
            dx=str(nums[0])
            n=len(nums)
            for pid, el in enumerate(nums):
                if idx!=el:
                    if dx!=str(nums[pid-1]):
                        dx+="->"+str(nums[pid-1])
                    dp.append(dx)
                    idx=el
                    dx=str(el)
                if pid==n-1:
                    if dx!=str(nums[pid]):
                        dx+="->"+str(nums[pid])
                    dp.append(dx)
                idx+=1
        return dp

                



            

