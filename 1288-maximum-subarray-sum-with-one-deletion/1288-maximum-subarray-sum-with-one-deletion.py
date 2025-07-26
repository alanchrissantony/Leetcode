class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dx=0
        dy=mx=arr[0]
        for idx in range(1,len(arr)):
            dx=max(dy, dx+arr[idx])
            dy=max(dy+arr[idx], arr[idx])
            curr=max(dx,dy)
            mx=max(mx,curr)
        return mx
