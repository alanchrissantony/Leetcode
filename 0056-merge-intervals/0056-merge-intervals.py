class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr=[]
        i=0
        n=len(intervals)
        while i<n:
            j=i+1
            flag=False
            x=intervals[i][0]
            y=intervals[i][1]
            
            while j<n and intervals[j][0] in range(intervals[i][0], intervals[i][1]+1) or j<n and intervals[j][1] in range(intervals[i][0], intervals[i][1]+1):
                    flag=True
                    x=min(intervals[j][0], x)
                    y=max(intervals[j][1], y)
                    intervals[i][0]=x
                    intervals[i][1]=y
                    j+=1
            if flag:
                arr.append([x,y])
                i=j
                continue
            arr.append(intervals[i])
            i+=1
        return(arr)