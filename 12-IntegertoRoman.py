class Solution:
    def intToRoman(self, num: int) -> str:
        dict={1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        i=num
        out=""
        while i>0:
            if i>=1000:
                i-=1000
                out+=dict[1000]
            elif i>=900:
                i-=900
                out+=dict[100]
                out+=dict[1000]
            elif i>=500:
                i-=500
                out+=dict[500]
            elif i>=400:
                i-=400
                out+=dict[100]
                out+=dict[500]
            elif i>=100:
                i-=100
                out+=dict[100]
            elif i>=90:
                i-=90
                out+=dict[10]
                out+=dict[100]
            elif i>=50:
                i-=50
                out+=dict[50]
            elif i>=40:
                i-=40
                out+=dict[10]
                out+=dict[50]
            elif i>=10:
                i-=10
                out+=dict[10]
            elif i>=9:
                i-=9
                out+=dict[1]
                out+=dict[10]
            elif i>=5:
                i-=5
                out+=dict[5]
            elif i>=4:
                i-=4
                out+=dict[1]
                out+=dict[5]
            else:
                i-=1
                out+=dict[1]
        return out
