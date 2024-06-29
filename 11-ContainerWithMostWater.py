class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        current=0
        left=0
        right=len(height)-1
        while left<right:
            current=max(current, min(height[left],height[right])*(right-left))
            area=max(area, current)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return area