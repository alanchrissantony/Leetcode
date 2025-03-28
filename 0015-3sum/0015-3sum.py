class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dp=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            left, right=i+1, len(nums)-1
            while left<right:
                dy=nums[i]+nums[left]+nums[right]
                
                if dy<0:
                    left+=1
                elif dy>0:
                    right-=1
                else:
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1 
                    
                    dp.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
        return dp