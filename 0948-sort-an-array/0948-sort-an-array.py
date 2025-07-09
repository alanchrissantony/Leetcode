class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left=nums[:mid]
        right=nums[mid:]

        return self.merge(self.sortArray(left), self.sortArray(right))


    def merge(self, left, right):
        arr=[]
        i=j=0
        m,n=len(left),len(right)
        while i<m and j<n:
            if left[i]<right[j]:
                arr.append(left[i])
                i+=1
            else:
                arr.append(right[j])
                j+=1
        arr.extend(left[i:])
        arr.extend(right[j:])

        return arr