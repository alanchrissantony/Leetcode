class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split(" ")
        arr=[]
        nums=[]
        i=0
        k=0
        while i<len(pattern):
            if pattern[i] in pattern[:i]:
                arr.append(pattern.index(pattern[i]))
            else:
                arr.append(k)
                k+=1
            i+=1
        i=0
        k=0
        while i<len(s):
            if s[i] in s[:i]:
                nums.append(s.index(s[i]))
            else:
                nums.append(k)
                k+=1
            i+=1
        print(arr, nums)
        return (arr==nums)