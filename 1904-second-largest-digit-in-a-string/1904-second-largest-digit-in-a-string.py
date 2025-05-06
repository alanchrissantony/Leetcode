class Solution:
    def secondHighest(self, s: str) -> int:
        dx=[]
        for el in s:
            if el.isdigit() and el not in dx:
                dx.append(el)
        dx.sort(reverse=True)
        return -1 if len(dx)<2 else int(dx[1])