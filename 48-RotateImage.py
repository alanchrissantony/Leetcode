from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i=0
        n=len(matrix)
        dp=[]
        l=0
        while i<n:
            j=0
            k=n-1
            dy=[]
            while j<n:
                dy.append(matrix[k][l])
                j+=1
                k-=1
            dp.append(dy)
            l+=1
            i+=1
        i=0
        while i<n:
            j=0
            while j<n:
                matrix[i][j]=dp[i][j]
                j+=1
            i+=1
        return matrix
        