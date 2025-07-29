class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        st=set()
        n,m=len(nums),0
        for idx in range(n):
            if nums[n-1-idx] <= k and nums[n-1-idx] not in st:
                st.add(nums[n-(idx+1)])
                m+=1
            if m>=k:
                break
        return idx+1
        