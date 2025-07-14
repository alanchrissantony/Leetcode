class Solution:
    def isValid(self, s: str) -> bool:
        lst=[s[0]]
        dt={'(':')', '{':'}', '[':']'}
        for idx in range(1, len(s)):
            if len(lst)>0 and lst[-1] in dt and dt[lst[-1]]==s[idx]:
                lst.pop()
            else:
                lst.append(s[idx])
        return len(lst)==0



