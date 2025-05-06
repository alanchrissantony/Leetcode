class Solution:
    def secondHighest(self, s: str) -> int:
        dx=[]
        for el in s:
            if el.isdigit() and int(el) not in dx:
                dx.append(int(el))
        dx.sort(reverse=True)
        print(dx)
        return -1 if len(dx)<2 else dx[1]