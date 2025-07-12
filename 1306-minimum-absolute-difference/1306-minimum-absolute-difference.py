class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        dp=[]
        diff=arr[-1]-arr[0]
        n=len(arr)
        for idx in range(1,n):
            diff=min(diff, arr[idx]-arr[idx-1])
        
        for idx in range(1,n):
            if arr[idx]-arr[idx-1]==diff:
                dp.append([arr[idx-1], arr[idx]])
        return dp