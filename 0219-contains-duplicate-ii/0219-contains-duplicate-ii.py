class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        dict={}
        i=0
        while i<n:
            if nums[i] in dict:
                if abs(dict[nums[i]]-i)<=k:
                    return(True)
                else:
                    dict[nums[i]]=i
            else:
                dict[nums[i]]=i
            i+=1
        return(False)