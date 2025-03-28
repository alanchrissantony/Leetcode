class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        arr=[]
        n=len(intervals)
        i=0
        check=True
        if n<1:
            return [newInterval]
        while i<n:
            j=i
            flag=False
            x=newInterval[0]
            y=newInterval[1]
            while j<n and intervals[j][0] in range(newInterval[0], newInterval[1]+1) or j<n and intervals[j][1] in range(newInterval[0], newInterval[1]+1):
                x=min(intervals[j][0],x)
                y=max(intervals[j][1],y)
                j+=1
                flag=True
            if flag:
                check=False
                arr.append([x,y])
                i=j

                continue
            elif newInterval[0] in range(intervals[i][0], intervals[i][1]+1) or newInterval[1] in range(intervals[i][0], intervals[i][1]+1):
                check=False
            arr.append(intervals[i])
            i+=1
        if check:
            arr.extend([newInterval])
            arr.sort()
        return(arr)