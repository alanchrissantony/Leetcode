class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        dx=""
        i=1
        for x in s[::-1]:
            if x=="-":
                continue
            dx+=x.upper()
            if i%k==0:
                dx+="-"
            i+=1
        dx=dx[::-1].strip("-")
        return dx