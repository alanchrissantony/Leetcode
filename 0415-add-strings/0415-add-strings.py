sys.set_int_max_str_digits(0)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sub=48
        n=len(num1)
        m=len(num2)
        dx=dy=0
        for idx, el in enumerate(num1):
            dx+=(10**(n-(idx+1)))*(ord(el)-sub)
        for idx, el in enumerate(num2):
            dx+=(10**(m-(idx+1)))*(ord(el)-sub)
        return str(dx+dy)