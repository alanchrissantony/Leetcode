class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        m,n=len(students), len(sandwiches)
        z=0
        while m>0 and n>0:
            i=0
            j=True
            while i<m:
                if students[i]==sandwiches[0]:
                    del students[i]
                    del sandwiches[0]
                    m-=1
                    n-=1
                    j=False
                i+=1
            if j:
                z+=1
            if z>m:
                break
        return len(students)
                    
                
