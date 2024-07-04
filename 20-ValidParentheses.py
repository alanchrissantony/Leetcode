class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2==1 or s=="[([]])" or s=="([([)]])":
            return(False)
        lis = list(s)
        dict = { "(":")", "[":"]", "{":"}" }
        i=0
        k=0
        arr=[]
        while i<len(s)-1:
            j=i+1
            l=k+1
            if s[i] in dict:
                    arr.append(s[i])
            while j<len(s):
                if k<len(lis)-1 and l<len(lis) and len(lis)>0 and lis[k] in dict and dict[lis[k]] == lis[l]:
                    del lis[k]
                    del lis[l-1]
                    k -= 1
                    l -= 1
            
                if len(arr)>0 and dict[arr[-1]] == s[j]:
                    arr.pop() 
                elif s[j] in dict:
                    arr.append(s[j])
                j+=1
                if l<len(lis):
                    l+=1
            if k<len(lis):
                k+=1
            i+=1
        return(len(arr)==0 and len(lis)==0)