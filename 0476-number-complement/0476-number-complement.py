class Solution:
    def findComplement(self, num: int) -> int:
        bn=list(format(num, 'b'))
        for idx, el in enumerate(bn):
            if el == '0':
                bn[idx]='1'
            else:
                bn[idx]='0'
        return int(''.join(bn), 2)
